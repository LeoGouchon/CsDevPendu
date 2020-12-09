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

#Personal Best Score
pb = 0
#Initialisation du programme
#On choisi un mot au hasard
word = fPendu.pickWord()
#Liste de toutes les lettres utilisés pas l'utilisateur
lstLetterUsed = [word[0]]
#Point de vie
hp = StringVar()
hp.set('8')
#Mot à afficher
dispWord = StringVar()
dispWord.set(fPendu.displayWord(word, lstLetterUsed))


mw = Tk()
mw.title("JEU DU PENDU")
mw.geometry('500x500')


def verif():
    if fPendu.finPartie(hp, word, lstLetterUsed) == False:
        mw.destroy()
        return
    #on fait séléctionner une lettre
    hp.set(fPendu.checkLife(hp, word, lstLetterUsed,letterScan.get()))
    dispWord.set(fPendu.displayWord(word, lstLetterUsed))
    
#Création bouton pour quitter le programme
buttonQuitt = Button(mw, text = "QUITTER", fg = "red", command = mw.destroy)
buttonQuitt.pack()

#Création de la zone de saisie de lettre et son label associé et son bouton pour valider
labelZoneSaisie = Label(mw, text = "Indiquer la lettre à étudier")
labelZoneSaisie.pack()

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

letterScan = StringVar()
zoneSaisie = Entry(mw, textvariable = letterScan)
zoneSaisie.focus_set()
zoneSaisie.pack()

#Affichage du mot et des points de vie de l'utilisateur
Label(mw, textvariable = dispWord).pack()
Label(mw, textvariable = hp).pack()

boutonSaisie = Button(mw, text = "valider ma lettre", command = verif)

mw.mainloop()