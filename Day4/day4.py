import numpy as np
from collections import defaultdict
import re
import datetime

inp = "in.txt"
entry = []
with open(inp) as f:
    for x in f.readlines():

        x  = x.rstrip().split(']')
        #year,month,date, hour, minutes = re.findall(x[0])
        timestamp = datetime.datetime.strptime(x[0][1:],'%Y-%m-%d %H:%M')
        entry.append((timestamp,x[1:]))


entry.sort(key = lambda elem: elem[0])

pattern = defaultdict(list)
total = defaultdict(int)
# 1973 : [fall_time, wake_time, fall_time, wake_time,...]

sleeping = False
for date, x in entry:
    info_str = x[0]
    if info_str[1] == 'G':
        guard = int(info_str.split()[1][1:])
    elif info_str[1] == 'f':
        if sleeping:
            print('Error, already sleeping')
        start = date.minute
        sleeping = True
    elif info_str[1] == 'w':
        if not sleeping:
            print("Error, already woke")
        end = date.minute
        pattern[guard].append((start,end))
        total[guard] += end-start
        sleeping = False

#print(pattern)
#print(total)

guard_idx = max(total, key = total.get)

sleeping_timetable = np.zeros((60,))
for start,end in pattern[guard_idx]:
    sleeping_timetable[start:end] += 1

#print(sleeping_timetable)
print(np.argmax(sleeping_timetable)*guard_idx)

##Part 2
most_frequent = defaultdict(int)

my_max = my_max_g = my_max_m = -1

#for every guard build freqeuency sleeping timetable and find
#the max value.
for g,t in pattern.items():
    sleeping = np.zeros((60,))
    for start, end in t:
        sleeping[start:end] += 1
    if np.max(sleeping) > my_max:
        my_max =  np.max(sleeping)
        my_max_m = np.argmax(sleeping)
        my_max_g = g

print(my_max_m*my_max_g)
