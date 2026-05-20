# -*- coding: utf-8 -*-
# Exercice 01 - Bilan d'ecoute au festival (gabarit)
"""
Objectif :
- DEMANDER : nom complet, spectacles electroniques, duree electronique, spectacles live, duree live
- Valider : spectacles >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Electronique: {A} spectacle(s), {He}h{Me:02d} d'ecoute
    Live: {B} spectacle(s), {Hl}h{Ml:02d} d'ecoute
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de spectacles electroniques assistes au festival : "
3) "Entrez la duree moyenne d'un spectacle electronique (en minutes) : "
4) "Entrez le nombre de spectacles live assistes au festival : "
5) "Entrez la duree moyenne d'un spectacle live (en minutes) : "
"""


try:
    nom = input( "Entrez votre nom complet : ")
    nbre_spectacle_electronique = int(input("Entrez le nombre de spectacles electroniques assistes au festival : "))
    duree_spectacle_electronique =int(input( "Entrez la duree moyenne d'un spectacle electronique (en minutes) : "))
    nbre_spectacle_live=int(input( "Entrez le nombre de spectacles live assistes au festival : "))
    duree_spectacle_live=int(input("Entrez la duree moyenne d'un spectacle live (en minutes) : "))
    
    


    if nbre_spectacle_electronique<0  or duree_spectacle_electronique <=0 or nbre_spectacle_live<0 or duree_spectacle_live<=0:
        print("Erreur - donnees invalides.")
    
        
# 
    else:
       
        duree_total_el = duree_spectacle_electronique * nbre_spectacle_electronique
        heure_electronique = duree_total_el // 60
        min_electronique = duree_total_el% 60
        duree_total_live= duree_spectacle_live * nbre_spectacle_live
        heure_live = duree_total_live // 60
        min_live = duree_total_live % 60
        duree_total = duree_total_el + duree_total_live
        heure_total = duree_total // 60
        min_total = duree_total % 60

        print(f"Bonjour {nom}")
        print(f"Electronique: {nbre_spectacle_electronique} spectacle(s), {heure_electronique}h{min_electronique:02d} d'ecoute")
        print(f"Live: {nbre_spectacle_live} spectacle(s), {heure_live}h{min_live:02d} d'ecoute")
        print(f"Total: {heure_total}h{min_total:02d}")
except:
    print("Erreur - donnees invalides.")


    
# TODO: Lire le nom (str)
#TODO: Calculer les minutes totales (electronique, live, total)
# TODO: Lire les 4 valeurs (int)

# TODO: Valider les donnees (spectacles >= 0, durees > 0)
# TODO: Convertir en heures/minutes et afficher exactement 4 lignes
