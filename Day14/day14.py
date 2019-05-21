#first simple simulation

from collections import deque

rank = [3,7]
e1 = 0
e2 = 1
recipes = 2
max_recipes = 793061
part1 = []
size2 = 0


for t in range(max_recipes + 10):
    s = rank[e1] + rank[e2]
    r1,r2 = s//10, s%10
 #   print(r1,r2)
    if r1!=0:
        rank.append(r1)
        recipes += 1
        if recipes > max_recipes:
            part1.append(r1)
            size2 += 1
            if size2 == 10:
                break

        rank.append(r2)
        recipes += 1
        if recipes > max_recipes:
            part1.append(r2)
            size2 += 1
            if size2 == 10:
                break
    else:
        rank.append(r2)
        recipes += 1
        if recipes > max_recipes:
            part1.append(r2)
            size2 += 1
            if size2 == 10:
                break

    e1 = (e1+rank[e1]+1)%len(rank)
    e2 = (e2+rank[e2]+1)%len(rank)

 #   print("After round:{}".format(rank))
 #   print(rank[e1],rank[e2])
#print(rank,e1,e2)
s = ''
for x in part1:
    s += str(x)
print(s)
#print("".join(str([x for x in part1])))
