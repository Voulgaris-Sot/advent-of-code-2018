inp = "in1.txt"
with open(inp) as f:
    change = [int(x) for x in f.readlines()]

#Part 1
print(sum(change))

#Part 2
from itertools import cycle

def find(change):
    seen = set([0])
    prev_len = -1
    freq = 0
    for c in cycle(change):
        freq += c
        seen.add(freq)
        cur_len = len(seen)
        if cur_len == prev_len:
            print(len(seen),"iterations")
            return freq
        else:
            prev_len = cur_len

print(find(change))
