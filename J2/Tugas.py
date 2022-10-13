def initial_graph():
    return {
        'A': {'C': 4, 'G': 9},
        'G': {'E': 6},
        'C': {'D': 6, 'H': 12},
        'D': {'E': 7},
        'H': {'F': 15},
        'E': {'F': 8},
        'F': {'B': 5},
        'B':{}
    }

initial = 'A'
path = {}
adj_node = {}
queue = []
graph = initial_graph()
for node in graph:
    path[node] = float("inf")
    adj_node[node] = None
    queue.append(node)

path[initial] = 0
while queue:
    key_min = queue[0]
    min_val = path[key_min]
    for n in range(1, len(queue)):
        if path[queue[n]] < min_val:
            key_min = queue[n]
            min_val = path[key_min]
    cur = key_min
    queue.remove(cur)

    for i in graph[cur]:
        alternate = graph[cur][i] + path[cur]
        if path[i] > alternate:
            path[i] = alternate
            adj_node[i] = cur

x = 'F'
print('Jalur A ke F')
print(x, end='<-')
while True:
    x = adj_node[x]
    if x is None:
        print("")
        break
    print(x, end='<-')