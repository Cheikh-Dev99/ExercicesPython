# Exercice 1 : Ecrire un programme qui stimule le service Orange Money
from Fonction import afficher_menu, afficher_factures, obtenir_nom_facture

OM = input(
    "\nBienvenue chez Orange, entrez le code du service de votre choix :\n"
)

while OM != "#144#":
    print("Code invalide. Veuillez entrer le code valide (Ex: #144#).")
    OM = input(
        "\nBienvenue chez Orange, entrez le code du service de votre choix :\n"
    )

solde = 250000

while True:
    afficher_menu()

    choix = int(input("\n==> "))

    if choix == 1:
        print(f"Le solde de votre compte est de {solde} F CFA.\n")
    elif choix == 2:
        montant = float(input("Entrez le montant à transférer : "))
        if montant <= 0:
            print("Le montant transféré doit être un nombre positif.")
            continue
        elif montant < 500:
            print(
                "Le montant transféré doit être supérieur ou égal à 500 F CFA."
            )
            continue
        numero = input("Entrez le numéro de destinataire : ")
        if solde < montant:
            print("Votre solde est insuffisant pour cette transaction.")
            continue
        solde -= montant
        print(f"\n{montant} F CFA ont été transférés au numéro {numero}.")
        print(f"Le nouveau solde de votre compte est de : {solde} F CFA\n")
    elif choix == 3:
        afficher_factures()
        choix_facture = int(input("Entrez le numéro de la facture à payer : "))
        numero_facture = input(
            "Entrez le N° de référence de la facture à payer (8 chiffres) :"
        )
        if len(numero_facture) != 8 or not numero_facture.isdigit():
            print("Le numéro de référence de la facture est invalide.")
            continue
        montant_facture = float(input("Entrez le montant de la facture : "))
        if solde < montant_facture:
            print("Votre solde est insuffisant pour cette transaction.")
            continue
        solde -= montant_facture
        nom_facture = obtenir_nom_facture(choix_facture)
        print(f"\nVotre facture {nom_facture} (N°{numero_facture}) de {
              montant_facture} F CFA a été payée.")
        print(f"Le nouveau solde de votre compte est de : {solde} F CFA\n")
    elif choix == 4:
        montant_credit = float(
            input("Entrez le montant de crédit à acheter : "))
        if solde < montant_credit:
            print("\nVotre solde est insuffisant pour cette transaction.")
            continue
        solde -= montant_credit
        print(f"\nVous avez acheté {montant_credit} F CFA de crédit.")
        print(f"Le nouveau solde de votre compte est de : {solde} F CFA\n")
    elif choix == 5:
        print("Merci d'avoir utilisé Orange Money. Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez entrer un numéro entre 1 et 5.")
        continue

    print("0. Retour à l'accueil Orange Money")
    print("1. Quitter")
    retour = int(input("\n==> "))
    if retour == 1:
        print("Merci d'avoir utilisé Orange Money. Au revoir!")
        break
