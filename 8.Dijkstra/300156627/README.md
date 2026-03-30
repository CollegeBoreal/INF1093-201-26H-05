# TP Dijkstra – INF1093

## 🏙️ Description du projet
Ce projet implémente l'**algorithme de Dijkstra** pour trouver le **plus court chemin** dans un graphe pondéré.  
Dans ce TP, les **sommets sont des villes** et les arêtes représentent les distances entre elles.  

L'objectif est de :  
- Créer un graphe avec des villes et des distances.  
- Trouver le chemin le plus court entre deux villes avec Dijkstra.  
- Visualiser le graphe et le chemin le plus court dans un notebook Jupyter.  

---

## 📁 Contenu du projet

| Fichier | Description |
|---------|-------------|
| `graph.py` | Contient les classes `Vertex` et `Graph` pour représenter le graphe. |
| `dijkstra_tp.py` | Contient la création du graphe, l'algorithme de Dijkstra et la reconstruction du plus court chemin. |
| `check_results.py` | Vérifie automatiquement si le chemin calculé est correct. |
| `RAPPORT.ipynb` | Notebook pour visualiser le graphe et mettre en évidence le chemin le plus court. |

---

## 🏙️ Graphe utilisé

Les villes et leurs connexions :

- **Paris** → Londres (7), Berlin (9), Bruxelles (14)  
- **Londres** → Berlin (10), Madrid (15)  
- **Berlin** → Madrid (11), Bruxelles (2)  
- **Madrid** → Rome (6)  
- **Rome** → Bruxelles (9)  

**Point de départ :** Paris  
**Destination :** Rome  

---

## 🚀 Comment exécuter le projet

1. Cloner le dépôt :  
```bash
git clone <lien_du_repo>
cd INF1093-201-26H-05/8.Dijkstra/300156627
