listes = []

while True:
    print("\nChoisissez parmi les 5 options suivantes :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")

    try:
        choix = int(input("👉 Votre choix : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    if choix == 1:
        e = input("Entrez le nom de l'élément à ajouter : ")
        if e.strip():  # Vérifie si l'entrée n'est pas vide
            listes.append(e)
            print(f"L'élément '{e}' a été ajouté à la liste.")
        else:
            print("L'élément ne peut pas être vide.")
        print("Liste actuelle :", listes)
        print("____________________________________")

    elif choix == 2:
        if len(listes) == 0:
            print("La liste est vide.")
        else:
            e = input("Entrez le nom de l'élément à retirer : ")
            if e in listes:
                confirmation = input(f"Êtes-vous sûr de vouloir retirer '{e}' ? (o/n) : ").lower()
                if confirmation == 'o':
                    listes.remove(e)
                    print(f"L'élément '{e}' a été retiré de la liste.")
                else:
                    print("Suppression annulée.")
            else:
                print(f"L'élément '{e}' n'est pas dans la liste.")
        print("Liste actuelle :", listes)
        print("____________________________________")

    elif choix == 3:
        if len(listes) == 0:
            print("La liste est vide.")
        else:
            print("La liste actuelle est :", listes)
        print("____________________________________")

    elif choix == 4:
        listes.clear()
        print("La liste a été vidée.")
        print("____________________________________")

    elif choix == 5:
        print("Au revoir")
        break

    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
        print("____________________________________")
