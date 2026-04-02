import sys

INF = 10**9

def min_distance(d1, d2):
    if d1 == "INF":
        return int(d2)
    if d2 == "INF":
        return int(d1)
    return min(int(d1), int(d2))

current_node = None
adj_list = ""
min_dist = INF
color = "WHITE"

def emit(node, adj, dist, col):
    dist_out = dist if dist != INF else "INF"
    print(f"{node}\t{adj}|{dist_out}|{col}")

for line in sys.stdin:
    line = line.strip()
    node, data = line.split("\t")
    adj, dist, col = data.split("|")

    if current_node and node != current_node:
        emit(current_node, adj_list, min_dist, color)
        adj_list = ""
        min_dist = INF
        color = "WHITE"

    current_node = node

    # Keep adjacency list
    if adj:
        adj_list = adj

    # Update distance
    if dist != "INF":
        min_dist = min(min_dist, int(dist))

    # Update color priority: BLACK > GRAY > WHITE
    if col == "BLACK":
        color = "BLACK"
    elif col == "GRAY" and color != "BLACK":
        color = "GRAY"

# Emit last node
if current_node:
    emit(current_node, adj_list, min_dist, color)