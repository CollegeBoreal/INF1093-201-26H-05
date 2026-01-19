# :o: Big-O

---

## 📌 **Qu’est-ce que la notation Big-O ?**

La **notation *Big-O*** est une façon de **décrire comment le coût (temps ou mémoire) d’un algorithme augmente quand la taille de l’entrée augmente**. Plutôt que de mesurer des secondes, on s’intéresse à **la croissance** : comment les ressources évoluent lorsque *n* (la taille des données) devient très grand. ([Wikipedia][1])

Elle ne donne pas une valeur exacte, mais elle **classe les algorithmes par efficacité** en mettant de côté :

* les **constantes** (ex. : 2 × n ? n) ;
* les **termes qui deviennent négligeables** pour de grandes tailles. ([Wikipedia][1])

---

## 📈 **Pourquoi l’utiliser ?**

Imagine que tu veux comparer deux façons de résoudre un problème (par exemple, trouver un élément dans une liste). Selon la façon dont le temps d’exécution **croît avec n**, un algorithme peut être très efficace, ou catastrophiquement lent pour de grandes entrées. ([Gist][2])

Grokké, cela signifie surtout :
👉 On ne compte pas précisément les opérations, on **regarde la tendance** quand *n* grandit. ([Gist][2])

---

## 📊 **Définition (formelle)**

On dit qu’une fonction *f(n)* est **O(g(n))** quand, pour des grandes valeurs de *n*, *f(n)* est au plus un **multiple constant de g(n)**.
Mathématiquement :
Il existe une constante *C > 0* et *n₀* telle que pour tout *n ≥ n₀* :

```
f(n) ≤ C × g(n)
```

Cela veut dire que *g(n)* est une **borne supérieure** (up-to-a-constant) de *f(n)* pour de grandes entrées. ([Grokipedia][3])

---

## 🧠 **Interprétation simple**

Pense à *n* comme à la **taille d’un problème** (par ex., nombre d’éléments dans un tableau) :

* ⭐ **O(1)** – *constant* : ne change presque jamais, même si n change.
* 📏 **O(n)** – *linéaire* : proportionnel à n.
* 📐 **O(n log n)** – *quasilinéaire* : un compromis, fréquent pour les tris efficaces.
* 🔁 **O(n²)** – *quadratique* : deux boucles imbriquées typiques.
* ⚠️ **O(n!)** – *factoriel* : explosion exponentielle, vite impraticable. ([Gist][2])

---

## 🧩 **Illustration avec des exemples concrets**

| Complexité     | Exemple d’algorithme typique           | Comment ça évolue               |             |
| -------------- | -------------------------------------- | ------------------------------- | ----------- |
| **O(1)**       | Accéder à un élément d’un tableau      | Inchangé quand *n* grandit      |             |
| **O(n)**       | Parcourir un tableau                   | Double *n* → double le temps    |             |
| **O(log n)**   | Recherche binaire dans un tableau trié | Très efficace, même grand *n*   |             |
| **O(n log n)** | Tri rapide (*quicksort*)               | Bonne performance sur grand *n* |             |
| **O(n²)**      | Tri naïf comme bubble sort             | Devient lent rapidement         | ([Gist][2]) |

---

## 🧠 **Ce qu’on ignore volontairement**

La notation Big-O **n’inclut pas** :

* les facteurs constants ;
* les petites variations qui ne changent rien à la croissance asymptotique. ([Wikipedia][1])

Par exemple :

```
3n² + 7n + 10 = O(n²)
```

Parce que pour de grandes valeurs de *n*, le terme *n²* domine le reste. ([Wikipedia][1])

---

## 📦 **Applications en informatique**

La Big-O sert à :

1. **Comparer les algorithmes** sans dépendre d’un matériel ou d’un langage ;
2. **Estimer l’évolution du coût** quand les données grossissent ;
3. **Choisir une solution plus scalable** pour de gros volumes. ([Grokipedia][3])

---

## 📌 **Résumé visuel**

* O(1) → constante
* O(log n) → logarithmique
* O(n) → linéaire
* O(n log n) → quasilinéaire
* O(n²), O(n³) → polynomiale
* O(cⁿ) ou O(n!) → exponentielle ou pire ([Gist][2])

---

[1]: https://en.wikipedia.org/wiki/Big_O_notation?utm_source=chatgpt.com "Big O notation"
[2]: https://gist.github.com/sunil-bagde/2b5c7ac60515514dc996038a23a6483b?utm_source=chatgpt.com "Grokking-Algorithms · GitHub"
[3]: https://grokipedia.com/page/Big_O_notation?utm_source=chatgpt.com "Big O notation"

