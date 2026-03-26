with open('entree\_insertion.txt', 'r') as f:

&#x20;   tab = list(map(int, f.read().split()))



def tri\_insertion(tab):

&#x20;   for i in range(1, len(tab)):

&#x20;       cle = tab\[i]

&#x20;       j = i - 1

&#x20;       while j >= 0 and tab\[j] > cle:

&#x20;           tab\[j + 1] = tab\[j]

&#x20;           j -= 1

&#x20;       tab\[j + 1] = cle



tri\_insertion(tab)

print('Résultat :', tab)

