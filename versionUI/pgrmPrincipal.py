"""
---------------------------
Créé le 27/11/2020
@author: leo.gouchon
---------------------------
Explication : Fichier contenant le code principal pour le jeu du pendu en version d'affichage Tkinter
Bug : 0 visualisé
To do list : /
Dernière modification : création du fichier
---------------------------
"""

from tkinter import Button, Tk, Label, StringVar, Entry

import fPendu

#CODE VERSION CLI A MODIFIER
#Personal Best Score
pb = 0

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

#Création fenêtre principale
mw = Tk()
mw.title("JEU DU PENDU")
mw.geometry('500x500')

#Création bouton pour quitter le programme
buttonQuitt = Button(mw, text = "QUITTER", fg = "red", command = mw.destroy)
buttonQuitt.pack()

#Création de la zone de saisie de lettre et son label associé et son bouton pour valider
labelZoneSaisie = Label(mw, text = "Indiquer la lettre à étudier")
labelZoneSaisie.pack()

lettreScan = StringVar() #La saisie sera sauvegardé ici pour l'utiliser dans les fonctions
zoneSaisie = Entry(mw, textvariable = lettreScan)
zoneSaisie.focus_set()
zoneSaisie.pack()

boutonSaisie = Button(mw, text = "valider ma lettre", command = fPendu.choiceLetter(lettreScan))

mw.mainloop()