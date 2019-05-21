#New approach with grid and simulations of bfs
#Now the order and the movement comes natural but not the search

inp = "in.txt"

from copy import deepcopy
from itertools  import count
import time
from collections import deque
import numpy as np
import sys

with open(inp) as f:
    grid = np.array([list(line.strip('\n')) for line in f], dtype = str)

class entity:

    hp = 200

    def __init__(self, x, y, unit):
        self.x = x
        self.y = y
        self.unit = unit
        self.power = 3
        self.alive = True

    def __repr__(self):
        return "{e.unit}({e.hp})".format(e=self)
        #return "X={e.x} Y={e.y} unit={e.unit} hp={e.hp}".format(e=self)

#construct a list with all entities
entities = []
for pos in np.argwhere(grid=='G'):
        entities.append(entity(pos[0],pos[1],'G'))
for pos in np.argwhere(grid=='E'):
        entities.append(entity(pos[0],pos[1],'E'))

entities.sort(key = lambda e: (e.x,e.y))

#will print the dead hp also
def print_grid(grid, entities):
    #could filter out the dead entities
    entities.sort(key = lambda e: (e.x,e.y)) #resort to be sure
    h,_ = grid.shape
    s = ''
    itr = iter(entities)
    nxt = next(itr)
    for i in range(h):
        s += ''.join(grid[i,:])
        while nxt.x == i:
            s += '\t' + str(nxt)
            try:
                nxt = next(itr)
            except StopIteration:
                break
        s += '\n'
    print(s)

def find_enemy(e, entities):
    enemies = []
    for ee in entities:
        if not ee.alive: continue
        if (abs(ee.x - e.x) + abs(ee.y - e.y) == 1) and (ee.unit != e.unit):
            enemies.append(ee)
    if enemies:
        enemies.sort(key = lambda e: (e.hp, e.x, e.y))
        return enemies[0]
    else:
        return None

def identify_targets(e, entities, grid):

    enemy_unit = 'E' if e.unit == 'G' else 'G'

    possible_targets = [pos for pos in np.argwhere(grid==enemy_unit)]
    if not possible_targets:
        return 0,None #Exit

    open_squares = []
    inplace = False
    for x,y in possible_targets:
        if (x-1==e.x or x+1==e.x) and y==e.y:
            inplace = True
            break
        if x==e.x and (y-1==e.y or y+1==e.y):
            inplace = True
            break

        if grid[x-1,y] == '.':
            open_squares.append([x-1,y])
        if grid[x+1,y] == '.':
            open_squares.append([x+1,y])
        if grid[x,y-1] == '.':
            open_squares.append([x,y-1])
        if grid[x,y+1] == '.':
            open_squares.append([x,y+1])

    if inplace:
        return 1,None #ready to attack

    if not open_squares:
        return 2,None #no move

    return 3, open_squares#ready to move

def neighbors(x, y, grid):
    neigh = []
    if grid[x-1,y] == ".":
        neigh.append([x-1,y])
    if grid[x,y-1] == ".":
        neigh.append([x,y-1])
    if grid[x,y+1] == ".":
        neigh.append([x,y+1])
    if grid[x+1,y] == ".":
        neigh.append([x+1,y])
    return neigh

#bfs with weight 1==shortest path
#set for quicker checking and deque for quicker popping
#https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3
def bfs(x, y, grid):
    #dont put time in bfs because it messes up the visited
    visited, queue = [[x, y]], [[x, y]]

    distance = {(x,y):0}

    while queue:
        v = queue.pop(0)
        for n in neighbors(v[0], v[1], grid):
            if n not in visited:
                distance[(n[0],n[1])] = 1+distance[(v[0],v[1])]
                visited.append(n)
                queue.append(n)

    return distance

def move(e,entities,grid,open_squares):

    distance = bfs(e.x, e.y, grid)
    #apo ta visited theloume na kratisoume mono ta open_squares
    reachable = {k:v for k,v in distance.items() if [*k] in open_squares} #mix up tuples and lists
    if not reachable:
        #print("No way for me")
        return

    chosen = sorted(reachable, key = lambda k: (reachable[k],k[0],k[1]))[0] #sort by time,then x then y

    possible_next = neighbors(e.x, e.y, grid)

    min_distance = 1e10
    for neigh in reversed(possible_next):
        distance = bfs(neigh[0], neigh[1], grid)
        if chosen in distance:
            if distance[chosen] <= min_distance:
                next_move = neigh
                min_distance = distance[chosen]

    #make the move
    grid[e.x,e.y] = '.'
    grid[next_move[0], next_move[1]] = e.unit
    e.x = next_move[0]
    e.y = next_move[1]

    return

print_grid(grid,entities)

def run_simulation(grid, entities):
    for r in count(1):
        entities.sort(key = lambda e: (e.x,e.y))
        for e in entities:

            if not e.alive: continue

            case, open_squares = identify_targets(e, entities, grid)

            if case == 0:
                print("no targets found.Exiting at round ",r)
                print_grid(grid, entities)
                print((r-1)*sum(e.hp for e in entities if e.alive))
                return entities
            elif case == 1:
                pass #ready to attack
            elif case == 2:
                continue #or pass #no moves
            elif case == 3:
                move(e,entities,grid,open_squares)

            enemy = find_enemy(e,entities)

            if enemy != None:
                enemy.hp -= e.power
                if enemy.hp <= 0:
                    enemy.alive = False
                    grid[enemy.x, enemy.y] = '.'
        #print("After Round ",r)
        #print_grid(grid,entities)

#Part1
run_simulation(np.copy(grid), deepcopy(entities))
#sys.exit()

#Part 2
def buff_Elves(entities, p):

    for e in entities:
        if e.unit == 'E':
            e.power = p
    return entities

#Manual seach because it is easier
#broad search in [10,20,30,40,50] to start and then narrow it down
#[21,23,25,27,29]
#Winner->25
for power in [25]:
    new_entities = buff_Elves(deepcopy(entities),power)
    remaining_entities = run_simulation(np.copy(grid), new_entities)

    end = True
    for e in remaining_entities:
        if e.alive and e.unit == 'G':
            print("Power = {}, Goblins won".format(power))
            end = False
            break
        if (e.unit == 'E') and (not e.alive):
            print("Power = {}, Elves won but there was a death".format(power))
            end = False
            break
    if end:
        print("Power = {}, Elves won without loss".format(power))
        break
