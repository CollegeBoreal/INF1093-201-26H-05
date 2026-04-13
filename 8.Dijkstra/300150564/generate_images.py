import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import numpy as np

# --- Données du graphe ---
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

edges = [
    ('Paris', 'Berlin', 1050),
    ('Paris', 'Madrid', 1270),
    ('Paris', 'Bruxelles', 305),
    ('Paris', 'Amsterdam', 480),
    ('Berlin', 'Rome', 1180),
    ('Berlin', 'Prague', 280),
    ('Berlin', 'Vienne', 680),
    ('Madrid', 'Rome', 1960),
    ('Rome', 'Vienne', 1130),
    ('Vienne', 'Prague', 290),
    ('Vienne', 'Bruxelles', 1130),
    ('Amsterdam', 'Bruxelles', 210),
    ('Bruxelles', 'Berlin', 900),
]

chemin = ['Paris', 'Berlin', 'Prague']
chemin_edges = [('Paris', 'Berlin'), ('Berlin', 'Prague')]

drapeaux = {
    'Paris': '🇫🇷', 'Berlin': '🇩🇪', 'Madrid': '🇪🇸',
    'Rome': '🇮🇹', 'Vienne': '🇦🇹', 'Amsterdam': '🇳🇱',
    'Bruxelles': '🇧🇪', 'Prague': '🇨🇿'
}

# ============================================================
# IMAGE 1 — Graphe principal avec chemin
# ============================================================
G = nx.Graph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

node_colors = ['#e74c3c' if n in chemin else '#3498db' for n in G.nodes()]
edge_colors = ['#e74c3c' if (e in chemin_edges or tuple(reversed(e)) in chemin_edges)
               else '#cccccc' for e in G.edges()]
edge_widths = [4 if (e in chemin_edges or tuple(reversed(e)) in chemin_edges)
               else 1.5 for e in G.edges()]

plt.figure(figsize=(14, 9))
plt.title('🗺️ Plus court chemin : Paris → Prague\nParis → Berlin → Prague  (1330 km)',
          fontsize=14, fontweight='bold', pad=20)

labels = {n: f"{drapeaux[n]} {n}" for n in G.nodes()}
nx.draw(G, pos=positions,
        node_color=node_colors,
        edge_color=edge_colors,
        width=edge_widths,
        labels=labels,
        node_size=1000,
        font_size=9,
        font_weight='bold')

edge_labels = {(u, v): f"{w} km" for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos=positions,
                              edge_labels=edge_labels,
                              font_size=7)

rouge = mpatches.Patch(color='#e74c3c', label='Chemin optimal')
bleu = mpatches.Patch(color='#3498db', label='Autres villes')
plt.legend(handles=[rouge, bleu], loc='lower left')
plt.tight_layout()
plt.savefig('images/graphe_dijkstra.png', dpi=150)
plt.close()
print("✅ Image 1 : graphe_dijkstra.png")

# ============================================================
# IMAGE 2 — Diagramme des distances depuis Paris
# ============================================================
distances = {
    'Berlin': 1050,
    'Madrid': 1270,
    'Bruxelles': 305,
    'Amsterdam': 480,
    'Rome': 2230,
    'Prague': 1330,
    'Vienne': 1435,
}

villes = list(distances.keys())
vals = list(distances.values())
colors = ['#e74c3c' if v == 'Prague' else '#3498db' for v in villes]

plt.figure(figsize=(10, 6))
bars = plt.bar(villes, vals, color=colors, edgecolor='black')
plt.title('📈 Distances depuis Paris vers chaque capitale', fontsize=13, fontweight='bold')
plt.xlabel('Ville')
plt.ylabel('Distance (km)')
plt.xticks(rotation=15)

for bar, val in zip(bars, vals):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20,
             f'{val} km', ha='center', va='bottom', fontsize=9)

rouge = mpatches.Patch(color='#e74c3c', label='Prague (destination)')
bleu = mpatches.Patch(color='#3498db', label='Autres villes')
plt.legend(handles=[rouge, bleu])
plt.tight_layout()
plt.savefig('images/distances_paris.png', dpi=150)
plt.close()
print("✅ Image 2 : distances_paris.png")

# ============================================================
# IMAGE 3 — Etapes de Dijkstra
# ============================================================
etapes = [
    ('Départ', 'Paris', 0),
    ('Étape 1', 'Bruxelles', 305),
    ('Étape 2', 'Amsterdam', 480),
    ('Étape 3', 'Berlin', 1050),
    ('Étape 4', 'Prague', 1330),
]

fig, ax = plt.subplots(figsize=(10, 5))
noms = [f"{e[0]}\n{e[1]}" for e in etapes]
vals = [e[2] for e in etapes]
colors = ['#2ecc71' if e[1] in ['Paris', 'Prague'] else '#3498db' for e in etapes]

bars = ax.bar(noms, vals, color=colors, edgecolor='black')
ax.set_title('🔄 Progression de Dijkstra : Paris → Prague', fontsize=13, fontweight='bold')
ax.set_ylabel('Distance cumulee (km)')

for bar, val in zip(bars, vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
            f'{val} km', ha='center', va='bottom', fontsize=10, fontweight='bold')

vert = mpatches.Patch(color='#2ecc71', label='Depart / Arrivee')
bleu = mpatches.Patch(color='#3498db', label='Etapes intermediaires')
ax.legend(handles=[vert, bleu])
plt.tight_layout()
plt.savefig('images/etapes_dijkstra.png', dpi=150)
plt.close()
print("✅ Image 3 : etapes_dijkstra.png")

print("\n🎉 Toutes les images generees dans images/")