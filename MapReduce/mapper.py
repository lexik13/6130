import sys

for line in sys.stdin:
    line = line.strip()
    node, data = line.split("\t")
    adj_list, dist, color = data.split("|")

    neighbors = adj_list.split(",") if adj_list else []

    # If current node is GRAY, expand it
    if color == "GRAY":
        for n in neighbors:
            print(f"{n}\t|{int(dist) + 1}|GRAY")

        # Mark current node as BLACK
        print(f"{node}\t{adj_list}|{dist}|BLACK")

    else:
        # Pass node as-is
        print(f"{node}\t{adj_list}|{dist}|{color}")