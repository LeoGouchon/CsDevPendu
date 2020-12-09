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

lettreScan = StringVar()
zoneSaisie = Entry(mw, textvariable = lettreScan)
zoneSaisie.focus_set()
zoneSaisie.pack()

mw.mainloop()