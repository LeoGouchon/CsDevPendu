"""
---------------------------
Créé le 27/11/2020
@author: leo.gouchon
https://github.com/LeoGouchon/CsDevPendu.git
---------------------------
Explication : Fichier contenant le code principal pour le jeu du pendu en version d'affichage Tkinter
---------------------------
"""

from tkinter import Button, Tk, Label, StringVar, Entry, IntVar, PhotoImage

import fPendu



#Création fenêtre principale
mw = Tk()
mw.title("JEU DU PENDU")
mw.geometry('500x500')


#--------Initialisation du programme--------
#Stockage des images dans une liste
image = [PhotoImage(file=f"./versionUI/bonhomme{9-i}.gif") for i in range(1,9)]
#Personal Best Score
pb = 0
#On choisi un mot au hasard
word = fPendu.pickWord()
#Liste de toutes les lettres utilisés pas l'utilisateur
lstLetterUsed = [word[0]]
#Point de vie
hp = IntVar()
hp.set(8)
#Mot à afficher
dispWord = StringVar()
dispWord.set(fPendu.displayWord(word, lstLetterUsed))

def verif():
    #Si la lettre est déjà utilisé, on clear la zone de saisie 
    if letterScan in lstLetterUsed : 
        zoneSaisie.delete(0, 'end')
        print("lettre déjà utilisé")
        return

    #On met à jour le nombre de point de vie selon la lettre entrée    
    hp.set(fPendu.checkLife(hp.get(), word, lstLetterUsed,letterScan.get()))
    dispWord.set(fPendu.displayWord(word, lstLetterUsed))
    dispImage.configure(image = image[hp.get()])
    zoneSaisie.delete(0, 'end')

    #Si la partie est fini
    if hp.get() < 0: 
        Label(mw, text = "DEFAITE!").pack()
        return

    if fPendu.displayWord(word, lstLetterUsed) == word : 
        Label(mw, text = "VICTOIRE!").pack()
        return
    return

#Création de la zone de saisie de lettre et son label associé et son bouton pour valider
labelZoneSaisie = Label(mw, text = "Indiquer la lettre à étudier")
labelZoneSaisie.pack()

letterScan = StringVar()
zoneSaisie = Entry(mw, textvariable = letterScan)
zoneSaisie.focus_set()
zoneSaisie.pack()

#Affichage du mot et des points de vie de l'utilisateur
Label(mw, textvariable = dispWord).pack()
Label(mw, textvariable = str(hp.get())).pack()

boutonSaisie = Button(mw, text = "valider ma lettre", command = verif)
boutonSaisie.pack()

#Image du pendu
dispImage = Label(mw, image = image[0])
dispImage.pack()

#Création bouton pour quitter le programme
buttonQuitt = Button(mw, text = "QUITTER", fg = "red", command = mw.destroy)
buttonQuitt.pack()

mw.mainloop()