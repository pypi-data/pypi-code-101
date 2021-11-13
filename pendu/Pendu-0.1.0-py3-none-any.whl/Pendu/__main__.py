__version__ = '0.1.0'


import os
from termcolor import colored
import string
import time
import platform
from art import tprint

def clear():
    if platform.system() == 'Windows':
        return 'cls'
    else:
        return 'clear'

global alphabet
alphabet = string.ascii_lowercase

class errors():
    wordLenghtError = colored('Oups...', 'red') + "Ton mot est trop court"
    wordError = colored('Oups...', 'red') + "Ton mot est étrange... Utilise seulement des lettres"
    letterError = colored('Oups...', 'red') + "Entre seulement ta lettre ou tape le mot en entier (3 lettres mini)."
    charError = colored('Oups...', 'red') + "Etrange, un caractère semble ne pas être une lettre, réessaie."
    usedLetter = colored('Oups...', 'red') + "Tu as déjà utilisé cette lettre, réessaie."

healthpoint = colored('♥', 'red')

clear = clear()


def getWord():
    global alphabet
    word = input('Entre ton mot (au moins 3 lettres) : ')
    word = word.lower()

    regular = True
    for char in word:
        if not char in alphabet+" -":
            regular = False
            break

    if len(word) >= 3:
        if regular:
            return word
        else:
            print(errors.wordError)
            return getWord()
    else:
        print(errors.wordLenghtError)
        return getWord()




def endGame(word, healthBar, turn, usedLetters, isWin):
    os.system(clear)
    print('')
    if isWin == False:
        tprint('GAME  OVER')
        print('')
        print('Dommage, tu feras mieux la prochaine fois...\n')
        print(colored('Réponse : ', 'yellow'), colored(word, 'green'))
        print(f'Lettres utilisées ({len(usedLetters)}) :', " ".join(usedLetters))
        print('Nombre de tours joués :', turn)

    else: 
        tprint('GAME  OVER')
        print('')
        print('Bien joué ! Tu as trouvé le mot !\n')
        print(colored("Il s'agissait bien de  ", 'yellow'), colored(word, 'green'))
        print(f'Lettres utilisées ({len(usedLetters)}) :', " ".join(usedLetters))
        print('Nombre de tours joués :', turn)

    print('Appuies sur entrée pour continuer.')
    input()
    tprint('Menu')
    print('\nQue souhaitez-vous faire ?\n')
    print('1) Rejouer -> Appuyez sur entrée.')
    print("2) Quitter -> Appuyez sur n'importe quelle touche, puis entrée.\n")

    toDo = input()
    if toDo == "":
        game()
    else:
        os.system(clear)
        tprint('A bientot !')
        quit()





def find(turn, word, healthBar, hidden, usedLetters):
    global alphabet
    
    

    os.system(clear)

    print("\n", healthpoint*healthBar + '♥'*(6 - healthBar), "\n\n", hidden, "\n\n", ' '.join(usedLetters))
    turn +=1
    letter = input("Quelle lettre veux-tu essayer ? Tapes le mot entier si tu pense l'avoir trouvé.\n\n     -> ")
    
    isOk = True
    for char in letter:
        if not char in alphabet + " -":
            isOk = False
            print(errors.charError)

    if isOk:
        print(letter)
        if len(letter) == 1 and not letter.upper() in str(usedLetters):
            
            usedLetters.append(letter.upper())
            
            if letter in word:
                                
                indexes = [i for i, j in enumerate(word) if j == letter]

                hidden = list(hidden)

                for i in indexes:
                    hidden[i] = letter
                    
                hidden = "".join(hidden)

                if hidden == word:
                    endGame(word, healthBar, turn, usedLetters, True)
                else:
                    find(turn, word, healthBar, hidden, usedLetters)
            else:
                healthBar -= 1
                if healthBar == 0:
                    endGame(word, healthBar, turn, usedLetters, False)
                else:
                    find(turn, word, healthBar, hidden, usedLetters)

        elif letter.upper() in usedLetters:
            print(errors.usedLetter)
            time.sleep(0.7)
            find(turn -1, word, healthBar, hidden, usedLetters)



        elif len(letter) == 2 :
            print(errors.letterError)
            time.sleep(2)
            find(turn -1, word, healthBar, hidden, usedLetters)

        else:
            if letter == word:
                endGame(word, healthBar, turn, usedLetters, True)
            else:
                print('\nMot incorrect, continue !')
                time.sleep(1)
                healthBar -= 1
                if healthBar == 0:
                    endGame(word, healthBar, turn, usedLetters, False)
                else:
                    find(turn, word, healthBar, hidden, usedLetters)





    else:
        time.sleep(1)
        find(turn -1, word, healthBar, hidden, usedLetters)



def game():
    
    os.system(clear)
    print("╔╗         ╔╗")
    print('║║╔═╗ ╔══╦═╣╚╗ ╔╗')
    print('║╚╣╩╣ ║║║║╬║╔╣ ╠╣')
    print('╚═╩═╝ ╚╩╩╩═╩═╝ ╚╝')

    word = getWord()
    print ('Ok, je jeu démarre bientôt.')
    time.sleep(1)
    os.system(clear)
    healthBar = 6
    
    hidden = word[0]+("_"*(len(word) -2))+word[-1]
    hidden = list(hidden)
    specialCharsAllowed = " -"
    indexes = [i for i, j in enumerate(word) if j in specialCharsAllowed]
    for i in indexes:
        hidden[i] = word[i]
    hidden = "".join(hidden)
    usedLetters = []
    find(0, word, healthBar, hidden, usedLetters)



if __name__ == "__main__":
    os.system(clear)
    print('╔╗╔╗')
    print('║╚╝╠═╗╔═╦╦═╦══╦═╗╔═╦╗')
    print('║╔╗║╬╚╣║║║╬║║║║╬╚╣║║║')
    print('╚╝╚╩══╩╩═╬╗╠╩╩╩══╩╩═╝')
    print('         ╚═╝')
    print('by PetchouDev\n')

    time.sleep(1.5)
    game()