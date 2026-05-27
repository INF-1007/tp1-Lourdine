# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le Parc Jean-Drapeau (gabarit)
"""
Objectif :
- DEMANDER : distance (km, float), attente_velo (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche = distance * 60 / 5 + controle
    velo   = attente_velo + distance * 60 / 15 + controle
    metro  = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "velo." ou "metro."
- 2 options ex-aequo (ordre : marcher, velo, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, velo et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au Parc Jean-Drapeau (en kilometres) : "
2) "Entrez le temps d'attente pour un velo en libre-service (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

import math
try:
    distance = float(input("Entrez la distance jusqu'au Parc Jean-Drapeau (en kilometres) : "))
    temps_velo = float(input("Entrez le temps d'attente pour un velo en libre-service (en minutes) : "))
    temps_metro=float(input( "Entrez le temps du trajet en metro (en minutes) : "))
    temps_controle = float(input( "Entrez le temps de controle a l'entree (en minutes) : "))

    if distance  < 0 or temps_velo < 0 or temps_metro < 0 or  temps_controle < 0:
        print("Erreur - donnees invalides.")
    
    
    else:
        marche = math.ceil(distance * 60 / 5 + temps_controle)
        velo =  math.ceil(temps_velo + distance * 60 / 15 + temps_controle)
        metro = math.ceil(temps_metro + temps_controle)

        minimum=min(marche,velo,metro)

        if  marche == velo== metro:
               print("Egalite : marcher, velo et metro.")

        elif marche == velo == minimum and minimum != metro:
            print("Egalite : marcher et velo.")

        elif metro == velo == minimum and minimum != marche:
              print("Egalite : metro et velo.")

        elif metro == marche == minimum and minimum != velo:
            print("Egalite : marcher et metro.")

        elif marche == minimum:
            print(f"Option la plus rapide : marcher.")

        elif velo == minimum:
            print(f"Option la plus rapide : velo.")

        elif metro == minimum:
            print(f"Option la plus rapide : metro.")

except:
        print("Erreur - donnees invalides.")


# TODO: Afficher la phrase exacte
#TODO: Lire les 4 valeurs

# TODO: Validation

# TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)