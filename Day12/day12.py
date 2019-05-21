inp = "in.txt"

rules = {}
with open(inp) as f:
    state = f.readline().rstrip()[15:]
    _ = f.readline()
    for x in f.readlines():
        rules[x[:5]] = x[9]

zero_pos = 0
Part1 = False
iterations = 20 if Part1 else 50000000000
for j in range(iterations):

    state = "..." + state + "..."
    n = '..'
    cnt = 0
    for i in range(2,len(state)-2):
        found = False #not needed if full rules
        for cond, res in rules.items():
            if state[i-2:i+3] == cond:
                n += res
                found = True
                break
        if not found:
            n += '.'
    n += '..'

    if n.lstrip('.').rstrip('.') == state.lstrip('.').rstrip('.'):
        print("Found the glider")
        print(state)
        print(n)
        state = n.lstrip('.').rstrip('.')
        break

    #basically you add the difference of the first plant pos
    #because of the padding the 2 strings are alligned
    zero_pos += -state.find('#') + n.find('#')
    n = n.lstrip('.').rstrip('.')
    state = n

#calculate the final zeros pos based on the fact we have a glider
if not Part1:
    zero_pos = zero_pos + (5000000000-j)

s = 0
for i,c in enumerate(state):
    if c == '#':
        s += i + zero_pos
print(s)
