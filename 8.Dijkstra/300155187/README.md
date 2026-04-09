# 🌍 TP Dijkstra – Réseau mondial

## 👤 Auteur
**Maimouna Diallo**  
ID : 300155187  

---

## 📌 Description
Ce projet implémente l’algorithme de **Dijkstra** pour calculer le **plus court chemin** entre plusieurs villes à travers le monde.  
Le graphe représente des villes de différents continents (Amérique, Europe, Afrique) avec des distances en kilomètres.

---

## 🌍 Continents et villes
- **Amérique du Nord** : Toronto, New York  
- **Europe** : London, Paris, Berlin, Rome  
- **Afrique** : Casablanca, Dakar, Lagos, Nairobi, Johannesburg  

---

## 🚀 Fonctionnalités
1. Calcul automatique du **plus court chemin** entre deux villes.  
2. Affichage de tous les chemins possibles pour comparaison.  
3. Visualisation **graphique** du réseau :  
   - Couleurs par continent  
   - Chemin optimal mis en évidence en vert  
   - Distances affichées sur chaque arête  

---

## 📏 Exemple de résultat

### 🖥️ Exécution dans PowerShell
![Résultat PowerShell](images/powershell_result.png)

**Chemin trouvé :**  
Toronto → London → Paris → Casablanca → Dakar → Lagos → Nairobi → Johannesburg  

**Distance totale :** 21240 km  

✅ Le chemin est correct !

---

### 🌐 Visualisation du graphe
![Graphe Dijkstra](images/graph_result.png)

- Le chemin optimal est affiché en **vert**
- Les autres chemins sont visibles en arrière-plan
- Les distances sont indiquées sur chaque connexion

---

## ⚙️ Technologies utilisées
- Python 🐍  
- NetworkX  
- Matplotlib  

---

## ▶️ Exécution du projet

### 📊 Lancer le notebook
```powershell
jupyter lab RAPPORT.ipynb

## ▶️ Exécution du projet

Dans PowerShell et Kernel:
```powershell 
jupyter lab RAPPORT.ipynb
<img width="485" height="342" alt="Dijkstra" src="https://github.com/user-attachments/assets/9d8c1bfa-5a1b-4bb9-bce5-c435d7c59a6a" />

python check_results.py
<img width="960" height="503" alt="capture python check_results" src="https://github.com/user-attachments/assets/e4021c8c-eb29-4b64-8fab-a534e90fe03f" />
