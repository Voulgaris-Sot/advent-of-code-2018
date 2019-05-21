inp = './in1.txt
with open(inp) as f:
    ids = [ x.rstrip() for x in f.readlines()]

from collections import defaultdict

#Part 1
twos = 0
threes = 0
for idx in ids:
    temp = defaultdict(int)
    for c in idx:
        temp[c] += 1
    if 2 in temp.values():
        twos += 1
    if 3 in temp.values():
        threes += 1

print("Part 1:",twos*threes)

#Part2
def diff1(id1,id2):
    cnt = 0
    for x,y in zip(id1, id2):
        if x == y:
            continue

        cnt += 1
        if cnt > 1:
            return False
    #in the case they are the same
    return cnt==1

from itertools import combinations

for c1,c2 in combinations(ids, 2):
    if diff1(c1,c2):
        #print(c)
        ans = ''
        for x,y in zip(c1,c2):
            if x==y:
                ans += x
        print("Part 2:", ans)
        break
