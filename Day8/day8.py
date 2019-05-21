from collections import defaultdict

inp = "in.txt"
with open(inp) as f:
    inp = [int(x) for x in f.readline().split()]

children = defaultdict(list)
metadata = defaultdict(list)
idx_global =  0
itr = iter(inp)
root = 0

def parse_tree(idx):

    global itr,idx_global
    no_childs = next(itr)
    no_metadata = next(itr)

    for i in range(no_childs):
        idx_global += 1
        children[idx].append(idx_global)
        parse_tree(idx_global)
    for i in range(no_metadata):
        metadata[idx].append(next(itr))

parse_tree(root)
#print(children,metadata)

print(sum(sum(meta) for meta in metadata.values()))

#Part 2
#cache intermediate results
all_values = defaultdict(int)
def evaluate(node):

    if not node in children:
        all_values[node] = sum(metadata[node])
        return

    #has children
    value = 0
    for meta in metadata[node]:
        if meta > len(children[node]) or meta == 0:
            continue
        child = children[node][meta-1]
        if child not in all_values:
            evaluate(child)
        value += all_values[child]

    all_values[node] = value

evaluate(root)
print(all_values[root])
