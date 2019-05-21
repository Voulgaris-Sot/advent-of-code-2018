inp = "in.txt"

import numpy as np
coords = []
with open(inp) as f:
    for x in f.readlines():
        c1,c2 = x.split(',')
        coords.append((int(c1),int(c2)))


#x goes right
#y goes down


left = min(coords, key = lambda x:x[0])[0]
right = max(coords, key = lambda x:x[0])[0]

top = min(coords, key = lambda x:x[1])[1]
down = max(coords, key = lambda x:x[1])[1]

#print("left = {}, right = {}, top = {}, down = {}".format(left,right,top,down))

size_x = down+1
size_y = right+1
grid = np.zeros((size_x, size_y),dtype = np.int64)
#print("Shape = ",grid.shape)

def man(i,j):

    min_i = -1
    min_d = 1e10
    for idx,c in enumerate(coords):
        dis = abs(i-c[0]) + abs(j-c[1])
        if dis < min_d:
            min_d = dis
            min_i = idx
        elif dis == min_d:
            min_i = -1
    return min_i


for i in range(0, size_y):
    for j in range(0, size_x):
        grid[j,i] = man(i,j)

#find values at perimeter
bad = set()
bad.update(np.unique(grid[0,:]))
bad.update(np.unique(grid[-1,:]))
bad.update(np.unique(grid[:,0])) ##Holy fuck!!!
bad.update(np.unique(grid[:,-1]))

counts = dict(zip(*np.unique(grid, return_counts = True)))

for b in bad:
    counts.pop(b)
print("bad",bad)
print(counts)

print(counts[max(counts, key = lambda x :counts[x])] )

#Part 2
limit = 10000
cnt = 0
for i in range(0, size_y):
    for j in range(0, size_x):
        s = 0
        offlimit = False
        for x,y in coords:
            s += abs(x-i)+abs(j-y)
            if s >= limit:
                offlimit = True
                break
        if not offlimit:
            cnt += 1
print(cnt)
