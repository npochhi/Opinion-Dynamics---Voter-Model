import networkx as nx
import random
import tqdm

graph = nx.fast_gnp_random_graph(1000, 0.5)

for n in graph:
  graph.nodes[n]['opinion'] = random.choice([-1, 1])

init_1 = 0
init__1 = 0

final_1 = 0
final__1 = 0

for n in graph:
  init_1 += 1 if graph.nodes[n]['opinion'] == 1 else 0
  init__1 += 1 if graph.nodes[n]['opinion'] == -1 else 0

print("Initial Ones: ", init_1)
print("Initial Minus Ones: ", init__1)

max_iter = 1000

for i in tqdm.tqdm(range(max_iter)):
  prev_graph = graph.copy()
  for n in prev_graph:
    graph.nodes[n]['opinion'] = random.choice([prev_graph.nodes[n1]['opinion'] for n1 in prev_graph.neighbors(n)])

for n in graph:
  final_1 += 1 if graph.nodes[n]['opinion'] == 1 else 0
  final__1 += 1 if graph.nodes[n]['opinion'] == -1 else 0

print("Initial Ones: ", final_1)
print("Initial Minus Ones: ", final__1)
