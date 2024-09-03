mots = []
print("Donnez-moi une liste de mots, et je vous dirai lequel est le plus long.")
nbr = int(input("Quel est le nombre de mots que vous souhaitez entrer : "))

print(f"Vous allez entrer une liste de {nbr} mots.")
for i in range(nbr):
    mot = input(f"Entrez le mot {i + 1} : ")
    mot_sans_espace = mot.replace(" ", "")
    mots.append(mot_sans_espace)

def longueur_mot_plus_long(mots):
    mot_plus_long = ""
    for mot in mots:
        if len(mot) > len(mot_plus_long):
            mot_plus_long = mot
    return mot_plus_long

mot_le_plus_long = longueur_mot_plus_long(mots)
print(f"Le mot le plus long de votre liste est : {mot_le_plus_long}")