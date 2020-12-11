"""
Créé le 27/11/2020
Par leo.gouchon
https://github.com/LeoGouchon/CsDevPendu.git
"""

import fPendu

#Personal Best Score
pb = 0

print("\nMeilleur score : ", pb)
choice = ""
while choice != 'oui' and choice != 'non':
    choice = input("Voulez-vous jouer ?\noui\nnon\n>>> ")
while choice == 'oui':
    #lance une partie
    hp=fPendu.partie()
    #résultat de la partie
    if hp == 0 :
        print("Vous avez perdu...")
    else :
        if hp >= pb:
            pb = hp
            print(20*"\n"+"Nouveau record : ",pb)
        print("Bravo vous avez gagné !")
    print("meilleur score : ", pb)
    #choix de l'utilisateur de continuer ou arreter
    choice = input("\nVoulez-vous jouer ?\noui\nnon\n>>> ")

