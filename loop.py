# on crée le tableau double dimension
table = [[" " for i in range(11)] for j in range(9)]

i = 0
middleTable = int(len(table[0]) / 2)
# permet de remplir le tableau avec des étoiles
while i < len(table):
    if i >= 0 and i < middleTable + 1:
        z = 0
        while z < i + 1:
            # permet de remplir la parti droite du tableau
            table[i][middleTable + z] = "*"
            # permet de remplir la parti gauche du tableau
            table[i][middleTable - z] = "*"
            z += 1
    if i >= middleTable + 1:
        k = middleTable - 1
        while k < middleTable + 2:
            table[i][k] = "*"
            k += 1

    i += 1

y = 0


print("le Sapin de Noël : ")
while y < len(table):
    print(" ".join(table[y]))  # permet d'afficher le tableau sans les crochets
    y += 1
