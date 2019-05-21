#solutionn based on the distance from the start. Good enough heuristic

import re
import copy
from itertools import count

pos = []
vel = []
inp = "in.txt"
with open(inp) as f:
    for x in f.readlines():
        num = list(map(int,re.findall(r'-?\d+',x)))
        pos.append([num[0],num[1]])
        vel.append([num[2],num[3]])

def print_message(pos):

    minx = min(x for x,_ in pos)
    maxx = max(x for x,_ in pos)

    miny = min(y for _,y in pos)
    maxy = max(y for _,y in pos)

    """
    minx = min(pos, key = lambda x:x[0])[0]
    miny = min(pos, key = lambda x:x[1])[1]
    maxx = max(pos, key = lambda x:x[0])[0]
    maxy = max(pos, key = lambda x:x[1])[1]
    """
    #should have used a str instead of printing
    for i in range(miny, maxy+1):
        for j in range(minx,maxx+1):
            if [j,i] in pos:
                print('#',end='')
            else:
                print('.',end='')
        print('')

initial_pos = copy.deepcopy(pos)
prev = 1e100

for t in count(0):
    #update position
    for i in range(len(pos)):
        pos[i][0] += vel[i][0]
        pos[i][1] += vel[i][1]

    #calculate distance from 0,0
    distance = sum(p[0]**2+p[1]**2 for p in pos)

    #whenever we see a not decreasing distance break
    if distance > prev:
        limit = t
        break

    prev = distance

print("The change happened at {} so expect the message shortly before".format(limit))

#don't have to to iterate over because of const velocity
#just search around the limit time

#fast forward
for i in range(len(initial_pos)):
    initial_pos[i][0] += vel[i][0]*(limit-5)
    initial_pos[i][1] += vel[i][1]*(limit-5)

#and print every message around
for t in range(limit - 5, limit+1):

    print(t)
    print_message(initial_pos)

    for i in range(len(initial_pos)):
        initial_pos[i][0] += vel[i][0]
        initial_pos[i][1] += vel[i][1]

