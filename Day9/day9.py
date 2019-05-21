from collections import defaultdict, deque
from tqdm import tqdm

inp = "in.txt"
with open(inp) as f:
    x = f.readline().split()
    no_players = int(x[0])
    last = int(x[6])

#Uncomment for part 2
#last*= 100

score = defaultdict(int)
x = deque([0])
player = -1

#for m in tqdm(range(1, last+1)):
for m in range(1, last+1):
    player = (player+1)%no_players

    if m%23 == 0:
        x.rotate(-7)
        score[player] += m
        score[player] += x.popleft()
        x.rotate(1)
    else:
        x.rotate(1)
        x.appendleft(m)

print(max(score.values()))
