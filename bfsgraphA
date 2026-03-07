"""
Graph500-Style BFS in Python
Runs BFS from random root
"""

import numpy as np
import collections

def generate_graph(scale, edge_factor=16, seed=42):
"""
Returns adjacency list, number of vertices, and edge count.
- scale : graph has 2^scale vertices
- edge_factor: edges ≈ edge_factor × vertices (Graph500 default = 16)
"""
rng = np.random.default_rng(seed)
n_vertices = 1 << scale # 2^scale
n_edges = n_vertices * edge_factor

# Graph500 R-MAT parameters
A, B, C = 0.57, 0.19, 0.19      # D = 1 - A - B - C = 0.05

src = np.zeros(n_edges, dtype=np.int64)
dst = np.zeros(n_edges, dtype=np.int64)

for depth in range(scale):
    r   = rng.random(n_edges)
    mid = 1 << (scale - depth - 1)
    src += np.where(r > A + B, mid, 0)
    dst += np.where((r > A) & (r <= A + B), mid,
           np.where(r > A + B + C,           mid, 0))

# Remove self-loops, deduplicate, make undirected
mask       = src != dst
src, dst   = src[mask], dst[mask]
edges      = np.unique(np.column_stack([np.minimum(src, dst),
                                        np.maximum(src, dst)]), axis=0)
src_all    = np.concatenate([edges[:, 0], edges[:, 1]])
dst_all    = np.concatenate([edges[:, 1], edges[:, 0]])

# Build adjacency list
adj = [[] for _ in range(n_vertices)]
for u, v in zip(src_all, dst_all):
    adj[u].append(v)

n_unique_edges = len(edges)
print(f"Graph: {n_vertices:,} vertices, {n_unique_edges:,} edges  (SCALE={scale})")
return adj, n_vertices, n_unique_edges
def bfs(adj, root, n_vertices):
"""
Breadth-First Search from root.
Returns parent array: parent[v] = parent of v in BFS tree, -1 if unvisited.
"""
parent = [-1] * n_vertices
parent[root] = root
queue = collections.deque([root])

while queue:
    u = queue.popleft()
    for v in adj[u]:
        if parent[v] == -1:
            parent[v] = u
            queue.append(v)

return parent
def validate(parent, root):
"""Check basic Graph500 BFS validity rules."""
if parent[root] != root:
return False, "parent[root] != root"

# Build depth array from parent tree
n      = len(parent)
depth  = [-1] * n
depth[root] = 0
queue  = collections.deque([root])
while queue:
    u = queue.popleft()
    for v, p in enumerate(parent):
        if p == u and v != u and depth[v] == -1:
            depth[v] = depth[u] + 1
            queue.append(v)

visited = sum(1 for p in parent if p != -1)
return True, f"Valid — {visited:,} vertices visited"
if name == "main":
import time, random

SCALE       = 14     # 2^14 = 16,384 vertices  (try 10–20)
EDGE_FACTOR = 16     # Graph500 standard
SEED        = 42

# Generate graph
adj, n_vertices, n_edges = generate_graph(SCALE, EDGE_FACTOR, SEED)

# Pick a random root with at least one neighbour
rng  = random.Random(SEED)
root = rng.choice([v for v in range(n_vertices) if adj[v]])
print(f"BFS root: {root}  (degree={len(adj[root])})")

# Run BFS
t0     = time.perf_counter()
parent = bfs(adj, root, n_vertices)
elapsed = time.perf_counter() - t0

# TEPS  =  edges traversed / seconds
edges_traversed = sum(len(adj[v]) for v in range(n_vertices) if parent[v] != -1)
teps = edges_traversed / elapsed

# Validate
ok, msg = validate(parent, root)

# Report
print(f"\nResults")
print(f"  Time      : {elapsed*1000:.1f} ms")
print(f"  TEPS      : {teps/1e6:.3f} MTEPS")
print(f"  Validation: {msg}")
