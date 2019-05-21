import re

inp = "in.txt"
with open(inp,'r') as f:
    dump = [list(map(int, re.findall(r'\d+',line))) for line in f]
    #remove empty lines
    dump = [d for d in dump if d]

all_commands = ["addr", "addi", "mulr","muli","banr","bani","borr","bori",
                "setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]

def execute(c, ins, reg):

    if   c == "addr":
        res = reg[ins[1]] + reg[ins[2]]

    elif c == "addi":
        res = reg[ins[1]] + ins[2]

    elif c == "mulr":
        res = reg[ins[1]] * reg[ins[2]]

    elif c == "muli":
        res = reg[ins[1]] * ins[2]

    elif c == "banr":
        res = reg[ins[1]] & reg[ins[2]]

    elif c == "bani":
        res = reg[ins[1]] & ins[2]

    elif c == "borr":
        res = reg[ins[1]] | reg[ins[2]]

    elif c == "bori":
        res = reg[ins[1]] | ins[2]

    elif c == "setr":
        res = reg[ins[1]]

    elif c == "seti":
        res = ins[1]

    elif c == "gtir":
        res = 1 if ins[1] > reg[ins[2]] else 0

    elif c == "gtri":
        res = 1 if reg[ins[1]] > ins[2] else 0

    elif c == "gtrr":
        res = 1 if reg[ins[1]] > reg[ins[2]] else 0

    elif c == "eqir":
        res = 1 if ins[1] == reg[ins[2]] else 0

    elif c == "eqri":
        res = 1 if reg[ins[1]] == ins[2] else 0

    elif c == "eqrr":
        res = 1 if reg[ins[1]] == reg[ins[2]] else 0

    else:
        print("No command")
        sys.exit()

    reg[ins[3]] = res

    return reg

part1 = 0
instructions_set = []
for i in range(0,len(dump),3):
    reg_before = dump[i]
    ins = dump[i+1]
    reg_after = dump[i+2]

    cnt = 0
    ins_set = set()
    for c in all_commands:
        reg_after_comm = execute(c, ins, reg_before.copy())
        if reg_after_comm == reg_after:
            ins_set.add(c)
            cnt +=1
    instructions_set.append(ins_set)

    if cnt >= 3:
        part1 += 1
print(part1)

#Part2
#First of all, for every instruction you keep all the possible explanations
#Then iteratively find an instruction with only one explanation
#and  remove it from all others explanations
#Do it 16 times for every command
code2commands = {}
for _ in range(16):
    for i,iset in enumerate(instructions_set):
        if len(iset) == 1:
            #guaranted to break
            break
    instructions_set = [x-iset for x in instructions_set]
    code2commands[dump[i*3+1][0]] = iset.pop()

print(code2commands)

with open("program.txt", 'r') as f:
    instructions = [list(map(int, re.findall(r'\d+',line))) for line in f]

#quick hack to reuse the previous function
regs = [0, 0, 0, 0]
for ins in instructions:
    regs = execute(code2commands[ins[0]],ins, regs.copy())
print(regs[0])

