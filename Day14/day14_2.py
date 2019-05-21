from itertools import count
rank = [3,7]
e1 = 0
e2 = 1
recipes = 2
inp = 793061
max_recipes = [int(d) for d in str(inp)]
size = len(max_recipes)
part1 = []
size2 = 0

for t in count(1):
    s = rank[e1] + rank[e2]
    r1,r2 = s//10, s%10
 #   print(r1,r2)
    if r1!=0:
        rank.append(r1)
        recipes += 1
        if rank[len(rank)-size:]==max_recipes:
            print(len(rank)-size)
            break

        rank.append(r2)
        recipes += 1

        if rank[len(rank)-size:]==max_recipes:
            print(len(rank)-size)
            break

       #rank.extend([r1,r2])
    else:
        rank.append(r2)
        recipes += 1

        if rank[len(rank)-size:]==max_recipes:
            print(len(rank)-size)
            break


    e1 = (e1+rank[e1]+1)%len(rank)
    e2 = (e2+rank[e2]+1)%len(rank)

