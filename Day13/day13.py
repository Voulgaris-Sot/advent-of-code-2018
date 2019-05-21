import sys
import numpy as np
import copy
from itertools import count

class cart:

    def __init__(self, c, x, y):
        self.c = c
        self.x = x
        self.y = y
        self.next = "l"
        self.alive = True

def print_grid(grid, carts):
    grid = grid.copy()
    for c in carts:
        if c.alive:
            grid[c.x, c.y] = c.c
    x,y = grid.shape
    s = ''
    for i in range(x):
        s += str(i)
        s += ''.join(grid[i,:])
        s += '\n'
    print(s)

inp = "in.txt"

with open(inp) as f:
    grid = np.array([list(line.strip('\n')) for line in f], dtype = str)


#find the position of carts
carts = []
for c in ["^","v",">","<"]:
    for pos in np.argwhere(grid==c):
        carts.append(cart(c,pos[0],pos[1]))

        #fix map (could use replace)
        if c == '^' or c == 'v':
            grid[pos[0],pos[1]] = '|'
        else:
            grid[pos[0],pos[1]] = '-'

print("Shape of grid", grid.shape)
print("Number of carts", len(carts))

#helper functions
def count_alive(carts):
    s = 0
    for c in carts:
        if c.alive:
            s += 1
    return s

def remove_if_collision(moving, carts, grid):
    for c in carts:
        if c.alive:
            if c.x == moving.x and c.y == moving.y and c.c != moving.c:
                c.alive = False
                moving.alive = False
                print("removing at", c.x, c.y)
                print("remaining:",count_alive(carts))

#start of simulation
for t in count(0):

    carts.sort( key = lambda c :(c.x, c.y))
    for cart in carts:

        if not cart.alive:
            continue

        #you have to check in the for loop because the collision might
        #happen later in this tick
        if count_alive(carts) == 1:
            for c in carts:
                if c.alive:
                    print(c.y,c.x,t)
            sys.exit()

        if cart.c == '^':
            cart.x -= 1
            x, y = cart.x, cart.y
            if grid[x,y] == '\\':
                cart.c = '<'
            elif grid[x,y] == '/':
                cart.c = '>'
            elif grid[x,y] == '+':
                if cart.next == 'l':
                    cart.c = '<'
                    cart.next = 's'
                elif cart.next == 's':
                    cart.next = 'r'
                elif cart.next == 'r':
                    cart.c = '>'
                    cart.next = 'l'
        elif cart.c == 'v':
            cart.x += 1
            x, y = cart.x, cart.y
            if grid[x,y] == '\\':
                cart.c = '>'
            elif grid[x,y] == '/':
                cart.c = '<'
            elif grid[x,y] == '+':
                if cart.next == 'l':
                    cart.c = '>'
                    cart.next = 's'
                elif cart.next == 's':
                    cart.next = 'r'
                elif cart.next == 'r':
                    cart.c = '<'
                    cart.next = 'l'
        elif cart.c == '>':
             cart.y += 1
             x, y = cart.x, cart.y
             if grid[x,y] == '\\':
                cart.c = 'v'
             elif grid[x,y] == '/':
                cart.c = '^'
             elif grid[x,y] == '+':
                if cart.next == 'l':
                    cart.c = '^'
                    cart.next = 's'
                elif cart.next == 's':
                    cart.next = 'r'
                elif cart.next == 'r':
                    cart.c = 'v'
                    cart.next = 'l'
        elif cart.c == '<':
             cart.y -= 1
             x, y = cart.x, cart.y
             if grid[x,y] == '\\':
                cart.c = '^'
             elif grid[x,y] == '/':
                cart.c = 'v'
             elif grid[x,y] == '+':
                if cart.next == 'l':
                    cart.c = 'v'
                    cart.next = 's'
                elif cart.next == 's':
                    cart.next = 'r'
                elif cart.next == 'r':
                    cart.c = '^'
                    cart.next = 'l'

        #Finally check for collisions
        remove_if_collision(cart,carts,grid)
