# Exercice 2 - Renvoyer le premier mot d’une chaîne de caractères

def premiermot(chaine):

# 0 est la position du premier mot
    return chaine.split()[0]

resultat = premiermot("Patrick prend son café latte")
print(resultat)
