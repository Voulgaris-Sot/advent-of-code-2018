inp = "in.txt"
with open(inp) as f:
     x = f.readline().rstrip()

#other solutions used a stack. I prefer my way of simply and efficiently iterating over
#but the cutting is a bit inefficient
def react(x):
    i = 0
    size = len(x)
    while i<size-1:
        if (x[i].lower() == x[i+1].lower() )and (x[i] != x[i+1]):
            x = x[:i] + x[i+2:]
            i = max(0,i-1)
            size -=2
        else:
            i += 1
    return size,x

part1, x = react(x)
print(part1)

#Part 2
#reuse x from part 1
min_c = len(x)+1

for unit in set(x.lower()):
    temp = x.replace(unit,"")
    temp = temp.replace(unit.upper(),"")

    c,_ = react(temp)
    min_c = min(c,min_c)

print(min_c)


