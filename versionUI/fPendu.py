"""
---------------------------
Créé le 27/11/2020
@author: leo.gouchon
---------------------------
Explication : Fichier contenant toutes les fonctions utiles pour le programme pendu en version Tkinter
Bug : def CheckLetter : le if ne sert à rien, il faut le changer pour obliger l'utilisateur à ré écrire une lettre
      def pickWorld : pb pour ouvrir le fichier, il ne trouve pas la source
To do list : /
---------------------------
"""

from random import randint

def pickWord():
    """
    fct qui choisi un mot aléatoire dans le fichier contenant tout les mots
    input : /
    output : un mot aléatoire
    """
    fichier = open('bddNomPendu.txt', 'r')
    allWord = (fichier.read()).split(" ")
    word = allWord[randint(0, len(allWord)-1)]
    fichier.close()
    return word


def choiceLetter(lstLetter, letter):
    """
    Fonction qui permet à l'utilisateur de choisir une lettre et vérifie sa pertinence
    input : lstLetter = liste des lettres déjà joué par l'utilisateur
    output : letter = la lettre choisie
    """
    if letter.isalpha()==False or letter in lstLetter or len(letter)>1:
        return False
    letter.lower()
    #Une fois une lettre valide, on l'a rajoute dans lstLetter
    lstLetter.append(letter)
    return letter


def checkLetter(word, lstLetter, letterUsed):
    """
    Fonction qui regarde si la lettre utilisé est dans le mot
    input : word = le mot à deviner
    output : True = lettre dans le mot
    output : False = lettre n'est pas dans le mot
    """
    letter = choiceLetter(lstLetter, letterUsed)
    #Pour le moment, le if ne fait rien
    if letter == False: 
        letter = choiceLetter(lstLetter, letterUsed)
    for i in range(len(word)):
        #Si letter est un caractère de word, return True
        if word[i] == letter : 
            return True
    return False


def checkLife(hp,word, lstLetter, letter):
    """
    Fonction qui actualise le nbr de vie selon la lettre selectionner
    input : hp = pt de vie de l'utilisateur
    output : hp = nouveau point de vie de l'utilisateur
    output : "fin de la partie" si hp == 0
    """
    if checkLetter(word, lstLetter, letter) == False:
        hp += -1
    #Si l'utilisateur n'a plus de vie, fin de la partie 
    return hp


def displayWord(word, lstLetter):
    """
    Fonction qui affiche le mot avec tout les lettres déjà utilisé
    input : word = mot aléatoire
    input : lstLetter = liste de toutes les lettres déjà utilisé par l'utilisateur
    output : wordHide = mot avec les '-' 
    """
    wordHide = word
    #On étudie chaque lettre du mot 
    for letterWord in word:
        #si la lettre n'est pas dans la liste des lettres rentrées par l'utilisateur, on la remplace par '_'
        if letterWord not in lstLetter:
            wordHide = wordHide.replace(letterWord, '-')                
    return wordHide


def finPartie(hp, word, lstLetter):
    """
    Fonction qui permet de voir si la partie est finie
    input : hp = pt de vie de l'utilisateur
    input : word = le mot à trouver
    input : lstLetter = liste des lettres utilisés
    output : True = Partie est finie
    output : False = Partie non finie
    """
    #Si l'utilisateur n'a plus de vie
    if hp <= 0 :
        return True
    #ou bien le mot avec les "_" est égal au mot complet
    elif displayWord(word, lstLetter) == word :
        return True
    #Si 1 des 2 possibilités de finir la partie n'est pas validée
    else :
        return False
    return


def partie():
    """
    Fonction qui lance une partie
    input : /
    output : hp = nbr de vie restante à la fin de la partie
    """

    """Initialisation de la partie"""
    word = pickWord()
    lstLetterUsed = [word[0]]
    #Point de vie
    hp = 8
    print('\nnbr de vie : ',hp)
    print(displayWord(word, lstLetterUsed))

    """Coeur de la partie"""
    while finPartie(hp, word, lstLetterUsed) == False :
        #on fait séléctionner une lettre
        hp = checkLife(hp, word, lstLetterUsed)
        print('\nnbr de vie : ',hp)
        print(displayWord(word, lstLetterUsed))
    return hp



"""---PARTIE TEST FONCTION---"""
"""------test pickWord------"""
#print(pickWord())
#print(choiceLetter())
#print(displayWord("choucroute",['o','c']))