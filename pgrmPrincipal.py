import fPendu

#Initialisation de la partie
word = fPendu.pickWord()
lstLetterUsed = [word[0]]
hp = 8
print('nbr de vie : ',hp)
print(fPendu.displayWord(word, lstLetterUsed))

#Coeur du code
while fPendu.finPartie(hp, word, lstLetterUsed) == False :
    #on fait séléctionner une lettre
    hp = fPendu.checkLife(hp, word, lstLetterUsed)
    displayWord(word)
