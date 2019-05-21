import numpy as np

inp = "in.txt"

claims = []
with open(inp) as f:
    for x in f.readlines():
        idx, _, start, dim = x.rstrip().split()

        #map(int,)
        claims.append((int(start.split(',')[0]),
                int(start.split(',')[1][:-1]),
                int(dim.split('x')[0]),
                int(dim.split('x')[1]),
                int(idx[1:])))


#Part 1
cloth = np.zeros((1000,1000),dtype = np.int32) #1000 is enough for my testcase

for x_start, y_start, wide, tall, _ in claims:
    cloth[y_start:y_start+tall, x_start:x_start+wide] += 1

print(np.where(cloth>1)[0].size)


#Part 2
for x_start, y_start, wide, tall, idx in claims:
    if np.all(cloth[y_start:y_start+tall, x_start:x_start+wide] == 1):
        print(idx)
        #break
