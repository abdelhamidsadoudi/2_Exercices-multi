# Exercice 4 - Ecrire un programme qui permet de retourne une phrase

def retourner_phrase(phrase):

# Séparer la phrase en mots
    mots = phrase.split(' ')

# Inverser l'ordre des mots
    mots_inverses = mots[::-1]

# Rejoindre les mots en une seule phrase
    return ' '.join(mots_inverses)

phrase = "J’en suis tout retourné"
print(retourner_phrase(phrase))
