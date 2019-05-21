#Another idea is to use partial sum.substract the one that go out the window and add the ones tha make it in
#but i believe partial sums are better
#from 2+ minutes to about 17 seconds
import numpy as np

grid = np.zeros((301,301))
#my input = 8561
serial = 8561

def powerlevel(x,y):
    global serial
    rack_id = x+10
    pl = rack_id*y
    pl += serial
    pl *= rack_id
    hundreds = (pl//100)%10
    return hundreds - 5

#x=j
#y=i
#fill the grid
for y in range(1,301):
    for x in range(1,301):
        grid[y,x] = powerlevel(x,y)

s = np.zeros_like(grid)
for y in range(1,301):
    for x in range(1,301):
        s[y,x] = np.sum(grid[1:y+1,1:x+1])


maxp = -100
for size in range(1,301):
    for y in range(1,301-size+1): #i think +1
        for x in range(1,301-size+1):
            #i think because 0 i dont mind getting a little out of bounds
            p = s[y+size-1,x+size-1] - s[y-1,x+size-1] - s[y+size-1,x-1] + s[y-1,x-1]
            if p > maxp:
                maxp = p
                maxx = x
                maxy = y
                maxs = size

print(maxp,maxx,maxy,maxs)

