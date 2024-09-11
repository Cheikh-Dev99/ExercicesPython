#Exercice Python : Trouvez le nombre mistère

import random

print("Trouves le nombre mystère entre 1 et 100 \n")

def play_game():
    x = random.randint(1, 100)
    nbr_attempts = 0

    while True:
        try:
            difficulty = int(input("Choisissez le niveau de difficulté entre : \n"
                                   "1 = Facile, 10 tentatives\n"
                                   "2 = Moyen, 8 tentatives\n"
                                   "3 = Difficile, 5 tentatives\n"
                                   "4 = Très-Difficile, 3 tentatives\n"
                                   "5 = Quitter le jeu\n"
                                   "👉 Votre choix : "))
            if difficulty == 1:
                attempts = 10
            elif difficulty == 2:
                attempts = 8
            elif difficulty == 3:
                attempts = 5
            elif difficulty == 4:
                attempts = 3
            elif difficulty == 5:
                print("Vous avez quitté le jeu. À la prochaine fois !")
                return
            else:
                print("\nVeuillez choisir un niveau de difficulté valide (1, 2, 3, ou 4).")
                continue
            break

        except ValueError:
            print("Veuillez entrer un nombre valide.\n")

    while attempts > 0:
        # print(x)
        try:
            y = int(input(f"\nVous-avez {attempts} tentatives \n"
                          "Entrez un nombre : "))
            while y < 1 or y > 100:
                print("Veuillez entrer un nombre entre 1 et 100.")
                y = int(input("Entrez un nombre : "))

            nbr_attempts += 1
            if y == x:
                print(f"\nBravo vous avez trouvé le nombre mystère {x} en {nbr_attempts} essaie{'s' if nbr_attempts > 1 else ''}\n")
                break
            elif y < x:
                print(f"Le nombre mystère est plus grand que {y}.")
            else:
                print(f"Le nombre mystère est plus petit que {y}.")

            attempts -= 1
            if attempts > 0:
                print(f"\nIl vous reste {attempts} tentative{'s' if attempts > 1 else ''}.")
            else:
                print(f"\nDésolé, vous avez utilisé vos {nbr_attempts} tentatives.\n"
                      f"Le nombre mystère était : {x}.\n")

        except ValueError:
            print("Veuillez réessayer et entrer un nombre entier valide entre 1 & 100.\n")

    res = input("Voulez-vous rejouer ? (o/n) : ")

    while res.lower() != 'o' and res.lower() != 'n':
        res = input("veuiller répondre par 'o' ou 'n' : ")

    if res.lower() == 'o':
        play_game()
    else:
        print("\nMerci d'avoir jouer à notre jeux, à la prochaine 😉")

play_game()
