# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets de festival (gabarit)
"""
Objectif :
- DEMANDER : n (int) et statut benevole (O/N)
- Options :
    20 journees : 80.00$
    10 journees : 44.00$
     4 journees : 18.00$
     1 journee  :  5.00$
- Reduction : si benevole = O, appliquer 10% de reduction sur le cout des forfaits uniquement.
  Les billets journaliers ne sont pas reduits.

But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, puis le plus petit nombre de billets journaliers

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 20 journees - A
    Forfaits de 10 journees - B
    Forfaits de 4 journees - C
    Billets journaliers - D
    Total billets - T
    Prix total - PPP.PP$

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut benevole (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""


try:
    n = int(input("Entrez le nombre de billets necessaires : "))
    statut = input("Entrez le statut benevole (O/N) : ")


    if n <0 or (statut != "N" and statut != "O"):
        print("Erreur - donnees invalides.")
   
        
    else:
        journees_20 = 80.00
        journees_10 = 44.00
        journees_4 = 18.00
        journee_1  =  5.00



        meilleur=float('inf')
        best_total = float('inf')
        best_d = float('inf')
        for i in range(n//20+1):
            for j in range(n//10+1):
                for k in range(n//4+1):
                    d=max(0, n - (i*20 + j*10 + k*4))
                    total_billet=(i*20)+(j*10)+(k*4)+d
                    
                    prix_total= (i*journees_20)+(j*journees_10)+(k*journees_4)+d*journee_1
                    if statut == "O":
                        rabais= 0.10 * (i*journees_20)+0.10*(j*journees_10)+0.1*(k*journees_4)
                        total_ben=prix_total-rabais
                        prix_final=total_ben
                    else:
                        prix_final=prix_total

                    if prix_final < meilleur or (prix_final == meilleur and total_billet < best_total) or (prix_final == meilleur and total_billet == best_total and d < best_d):
                        meilleur = prix_final
                        best_i = i
                        best_j = j
                        best_k = k
                        best_d = d
                        best_total = total_billet
        print(f"Forfaits de 20 journees - {best_i}")
        print(f"Forfaits de 10 journees - {best_j}")
        print(f"Forfaits de 4 journees - {best_k}")
        print(f"Billets journaliers - {best_d}")
        print(f"Total billets - {best_total}")
        print(f"Prix total - {meilleur:.2f}$")
except:
    print("Erreur - donnees invalides.")


# TODO: Calculer et afficher le resultat exact (6 lignes)
# TODO: Lire n (int) et statut (str)
# TODO: Validation (n >= 0 et statut dans {O, N})
# TODO: Chercher la meilleure combinaison (A, B, C, D)