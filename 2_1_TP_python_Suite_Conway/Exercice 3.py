# Exercice 3 - Mettre en majuscule la première lettre de chaque mot

def majuscule_mot(chaine):

# Séparer la chaîne en mots
    mots = chaine.split(' ')

# Mettre en majuscule la première lettre de chaque mot
    mots_majuscule = [mot.capitalize() for mot in mots]

# Rejoindre les mots en une seule chaîne
    return ' '.join(mots_majuscule)

phrase = "je mange du fromage"
print(majuscule_mot(phrase))
