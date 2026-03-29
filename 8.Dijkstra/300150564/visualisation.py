# visualisation.py
import networkx as nx
import matplotlib.pyplot as plt
from dijkstra_tp import g, shortest

# --- Reconstruction du chemin Paris → Prague ---
target = g.get_vertex('Prague')
path = shortest(target)
path_edges = list(zip(path, path[1:]))

# --- Création du graphe NetworkX ---
G = nx.Graph()

for v in g:
    for w in v.get_connections():
        G.add_edge(v.get_id(), w.get_id(), weight=v.get_weight(w))

# --- Positions des villes sur la carte ---
positions = {
    'Paris':      (2.3, 48.9),
    'Berlin':     (13.4, 52.5),
    'Madrid':     (-3.7, 40.4),
    'Rome':       (12.5, 41.9),
    'Vienne':     (16.4, 48.2),
    'Amsterdam':  (4.9, 52.4),
    'Bruxelles':  (4.4, 50.8),
    'Prague':     (14.4, 50.1),
}

# --- Couleurs ---
node_colors = ['#e74c3c' if n in path else '#3498db' for n in G.nodes()]
edge_colors = ['#e74c3c' if e in path_edges or tuple(reversed(e)) in path_edges
               else '#cccccc' for e in G.edges()]
edge_widths = [4 if e in path_edges or tuple(reversed(e)) in path_edges
               else 1.5 for e in G.edges()]

# --- Affichage ---
plt.figure(figsize=(12, 8))
plt.title("Plus court chemin : Paris → Prague\n" + " → ".join(path) +
          f"  ({target.get_distance()} km)", fontsize=14, fontweight='bold')

nx.draw(G, pos=positions,
        node_color=node_colors,
        edge_color=edge_colors,
        width=edge_widths,
        with_labels=True,
        node_size=800,
        font_size=10,
        font_weight='bold')

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=labels, font_size=8)

plt.tight_layout()
plt.savefig('graphe_dijkstra.png')
plt.show()
print("✅ Image sauvegardée : graphe_dijkstra.png")