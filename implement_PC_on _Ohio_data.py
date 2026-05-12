import pandas as pd
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.GraphUtils import GraphUtils

# Load lagged dataframe
df = pd.read_csv("tests/TestData/ohio_cbg_hr_lagged.csv")

print(df.head())
print(df.shape)

# Convert to numpy
X = df.to_numpy()

# Variable names
labels = df.columns.tolist()

# Run PC algorithm
cg = pc(
    X,
    alpha=0.05,
    indep_test="fisherz"
)

# Save graph
pyd = GraphUtils.to_pydot(
    cg.G,
    labels=labels
)

print(cg.G)
import networkx as nx
import matplotlib.pyplot as plt
import os

G = nx.Graph()   # undirected for now, because many PC edges are "---"

for edge in cg.G.get_graph_edges():
    n1 = edge.node1.get_name()   # e.g. "X1"
    n2 = edge.node2.get_name()   # e.g. "X3"

    # convert X1 -> labels[0], X2 -> labels[1], etc.
    idx1 = int(n1[1:]) - 1
    idx2 = int(n2[1:]) - 1

    G.add_edge(labels[idx1], labels[idx2])

plt.figure(figsize=(12, 8))
nx.draw(
    G,
    with_labels=True,
    node_size=3000,
    font_size=8
)

save_path = os.path.abspath("ohio_networkx_graph.png")
plt.savefig(save_path, bbox_inches="tight")

print(f"Graph saved at:\n{save_path}")

plt.show()

save_path = os.path.abspath("ohio_networkx_graph.png")

plt.savefig(save_path)

print(f"Graph saved at:\n{save_path}")

plt.show()