"""
---------------------------
Créé le 27/11/2020
@author: leo.gouchon
https://github.com/LeoGouchon/CsDevPendu.git
---------------------------
Explication : Fichier contenant le code principal pour le jeu du pendu en version d'affichage Tkinter
Problème(s) du code : 
On ne peut pas relancer de partie
---------------------------
"""

from tkinter import Button, Tk, Label, StringVar, Entry, IntVar, PhotoImage

import fPendu

#Création fenêtre principale tkinter
mw = Tk()
mw.title("JEU DU PENDU")
mw.geometry('500x500')
mw.configure(bg = '#1f3c88')

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

#Fonction appelé à chaque fois que l'utilisateur valide une lettre avec le bouton buttonSaisie
def verif():
    zoneSaisie.configure(bg = 'white')
    #Si la lettre est déjà utilisé, on clear la zone de saisie et on met un fond rouge pour indiquer une erreur à l'utilisateur
    if (letterScan.get()).lower() in lstLetterUsed or len(letterScan.get()) > 1 or (letterScan.get()).isalpha() == False: 
        zoneSaisie.delete(0, 'end')
        zoneSaisie.configure(bg = '#ee6f57')
        return

    #On met à jour le nombre de point de vie selon la lettre entrée 
    else :  
        hp.set(fPendu.checkLife(hp.get(), word, lstLetterUsed,(letterScan.get()).lower()))
        dispWord.set(fPendu.displayWord(word, lstLetterUsed))
        zoneSaisie.delete(0, 'end') 
        dispImage.configure(image = image[hp.get()])
        
    #Si la partie est finie
    #en perdant : 
    if hp.get() < 0: 
        wordFind.configure(textvariable = word ,bg = '#ee6f57', fg = '#f6f5f5')
        buttonSaisie.pack_forget()
        zoneSaisie.pack_forget()
        labelZoneSaisie.configure(text = "DEFAITE !")
        return
    #en gagnant : 
    if fPendu.displayWord(word, lstLetterUsed) == word : 
        wordFind.configure(bg = '#070d59', fg = '#f6f5f5')
        buttonSaisie.pack_forget()
        zoneSaisie.pack_forget()
        labelZoneSaisie.configure(text = "VICTOIRE !")
        return
    return

#Création de la zone de saisie de lettre et son label associé et son bouton pour valider
labelZoneSaisie = Label(mw, text = "Indiquer la lettre à étudier", bg = '#1f3c88', fg = '#f6f5f5')
labelZoneSaisie.pack()
letterScan = StringVar()
zoneSaisie = Entry(mw, textvariable = letterScan, bg = '#f6f5f5')
zoneSaisie.focus_set()
zoneSaisie.pack()
buttonSaisie = Button(mw, text = "valider ma lettre", bg = "#f6f5f5", command = verif)
buttonSaisie.pack()

#Affichage du mot à deviner
wordFind = Label(mw, textvariable = dispWord, width = "12", font=("Courier", 30), bg = "#f6f5f5")
wordFind.pack()

#Image du pendu
dispImage = Label(mw, image = image[0])
dispImage.pack()

#Création bouton pour quitter le programme
buttonQuitt = Button(mw, text = "QUITTER", fg = "black", bg = "#ee6f57", borderwidth = 3, command = mw.destroy)
buttonQuitt.pack(side = "bottom")

mw.mainloop()