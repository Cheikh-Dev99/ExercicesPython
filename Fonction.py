def afficher_factures():
    print("1. SENELEC")
    print("2. SONATEL")
    print("3. SEN'EAU")
    print("4. BAKELI")


def obtenir_nom_facture(num_facture):
    factures = {
        1: "SENELEC",
        2: "SONATEL",
        3: "SEN'EAU",
        4: "BAKELI"
    }
    return factures.get(num_facture, "Inconnu")


def afficher_menu():
    print("\nBienvenue chez Orange Money")
    print("Vous pouvez effectuer les opérations suivantes : ")
    print("1. Solde de mon compte")
    print("2. Transfert d'argent")
    print("3. Paiement de facture")
    print("4. Achat de crédit")
    print("5. Quitter")
