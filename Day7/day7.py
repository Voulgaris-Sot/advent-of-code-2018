inp = "in.txt"

import networkx as nx
import time as time1

G = nx.DiGraph()
with open(inp) as f:
    for x in f.readlines():
        x = x.split()
        G.add_node(x[1])
        G.add_node(x[7])
        G.add_edge(x[1],x[7])

part1 = ""
for e in nx.lexicographical_topological_sort(G):
    part1 += e
print(part1)

#Part2
#interesting to do in parallel
#or to traverse the graph
#If multiple steps are available, workers should still begin them in alphabetical order

time_delay = 60
time = {n: 1 + time_delay + ord(n) - ord('A') for n in G.nodes()}


tt = 0
next_nodes = []
done = ""
total_workers = 6
working = 0

given = {x:False for x in G.nodes() }
G_r = G.reverse()

#assign initial jobs
ready_nodes = sorted([x for x in G_r.nodes if list(G_r.neighbors(x))==[]])
for nn in ready_nodes:
    if working == total_workers:
        break
    if given[nn]:
        continue
    next_nodes.append((tt + time[nn], nn))
    working += 1
    given[nn] = True


while len(done) != G.number_of_nodes():
    #time1.sleep(1)

    for t, n in list(next_nodes):
        if tt<t:
            continue

        #found a node that's finished
        G_r.remove_node(n)
        working -= 1
        done += n

        #assign a job
        ready_nodes = sorted([x for x in G_r.nodes if list(G_r.neighbors(x))==[]])

        for nn in ready_nodes:
            if working == total_workers:
                break
            if given[nn]:
                continue

            next_nodes.append((tt + time[nn], nn))

            working += 1
            given[nn] = True

    #remove done nodes
    next_nodes = [ x for x in next_nodes if x[1] not in done]
    #print(tt, next_nodes, ready_nodes)
    #print(given)
    tt += 1

print(tt-1)
