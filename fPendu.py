from random import randint

def pickWord():
    """
    fct qui choisi un mot aléatoire dans le fichier contenant tout les mots
    input : /
    output : un mot aléatoire
    """
    fichier = open('bddNomPendu.txt', 'r')
    allWord = (fichier.read()).split(" ")
    word = allWord[randint(0, len(allWord))]
    fichier.close()
    return word


def choiceLetter():
    """
    Fonction qui permet à l'utilisateur de choisir une lettre
    On pourra rajouter des sécurités sur le choix de la lettre
    input : /
    output : letter = la lettre choisie
    """
    letter = input('Choisissez votre lettre :\n>>>')
    while letter not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        letter = input('Choisissez votre lettre :\n>>>')
    return letter


def checkLetter(word):
    """
    Fonction qui regarde si la lettre utilisé est dans le mot
    input : word = le mot à deviner
    output : True = lettre dans le mot
    output : False = lettre n'est pas dans le mot
    """
    letter = choiceLetter()
    for i in range(len(word)):
        #Si letter est un caractère de word, return True
        if word[i] == letter : 
            return True
    return False


def checkWord(word, lstLetter):
    """
    Fonction qui affiche le mot avec tout les lettres déjà utilisé
    input : word = mot aléatoire
    input : lstLetter = liste de toutes les lettres déjà utilisé par l'utilisateur
    output : wordHide = mot avec les '_' 
    """
    wordHide = word
    #On étudie chaque lettre du mot 
    for letterWord in word:
        #si la lettre n'est pas dans la liste des lettres rentrées par l'utilisateur, on la remplace par '_'
        if letterWord not in lstLetter:
            wordHide = wordHide.replace(letterWord, '_')                
    return wordHide


def checkLife(hp,word):
    """
    Fonction qui actualise le nbr de vie selon la lettre selectionner
    input : hp = pt de vie de l'utilisateur
    output : hp = nouveau point de vie de l'utilisateur
    output : "fin de la partie" si hp == 0
    """
    if checkLetter(word) == False:
        hp += -1
    #Pas sûr de ça
    #Si l'utilisateur n'a plus de vie, fin de la partie 
    if hp <= 0 :
        print("FIN DE LA PARTIE")
    return



"""---PARTIE TEST FONCTION---"""
"""------test pickWord------"""
#print(pickWord())
#print(choiceLetter())
#print(checkWord("choucroute",['o','c']))