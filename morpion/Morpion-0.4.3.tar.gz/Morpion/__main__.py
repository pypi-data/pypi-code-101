#coding = utf-8
__version__ = '0.4.3'

import random
from termcolor import colored, cprint
import platform
import time
from art import *
import os
import json
import getpass
import uuid
from Morpion.datas import variables, loading, setGrid, getPlayers, notDone, isWinner 



pathToScript = os.path.dirname(os.path.abspath(__file__))


def pathToSave()->str:
    if platform.system() == 'Windows':
        usr = str(getpass.getuser())
        usr = usr[:5]
        path = str(r"c:/Users/{}/PCCorp".format(usr))
        return path
    else:
        return f"/Users/{getpass.getuser()}/PCCorp"

print(__name__)




vars = variables()
colors = vars.colors
cases = vars.scheme
title = vars.title
commands = {"Windows": ["cls", "exit", "python -m Morpion"], "Linux":["clear", "exit", """
        python3 -m Morpion
        """], "Darwin": ["clear", "", """
        python3 -m Morpion
        """] }

sys = platform.system()



global joueurs
joueurs = []



global Player1
Player1 = colored("X", colors[2])
global Player2
Player2 = colored("O", colors[0])



global coup
coup = 0

global casesDispo
casesDispo = []

            
def getCoup(p, casesDispo) -> int:
    coup = "test"
    while not str(coup) in str(casesDispo):
        coup = input(f'{p}, quelle case veux-tu marquer ?  ')
        if coup == "":
            coup = "lol"
        try:
            coup = int(coup)
        except ValueError:
            print('Choisi une case disponible (numéros visibles)')
            pass
    return coup 
    
    


def setGame(joueurs, gameManager):

    for p in gameManager['currentPlayers']:
        joueurs.append(p)
    grid = setGrid(1, 0, 0)
    os.system(commands[sys][0])
    for ligne in grid:
        print(ligne)
    game(joueurs, gameManager)

def game(joueurs, gameManager):
    casesDispo = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    turn = 1
    p1 = random.choice(joueurs)
    #print(joueurs)
    p2 = random.choice(joueurs)
    while p2== p1:
        p2 = random.choice(joueurs)
    while notDone(turn):
        turn = turn+1
        if turn%2 == 1:
            p = p1
        else:
            p = p2
        
        coup = getCoup(p, casesDispo)
        try:
            casesDispo.remove(coup)
        except ValueError:
            pass
        #print(casesDispo)
        
        if turn%2 == 1:
            newGrid = setGrid(turn, coup, Player1)
        else:
            newGrid = setGrid(turn, coup, Player2)
        os.system(commands[sys][0])
        for ligne in newGrid:
            print(ligne)



    time.sleep(2)
    os.system(commands[sys][0])
    
    """print(p)
    print(type(p))
    print(p1)
    print(type(p1))
    print(p2)
    print(type(p2))
    print(gameManager)"""

    
    
    if isWinner() == False:
        trun = 9
    else: 
        turn = 11
    EndScreen(turn, gameManager, p1, p2, p)



def eraseDatas(turn, gameManager, p1, p2, p):
    captcha = str(uuid.uuid4())
    captcha = captcha[:5]
    print('recopier les caractères suivants pour confirmer : ' + captcha)
    
    a = input('-> ')
    if a == captcha:
        gameManager = {"# Error 509 TroubleShooter" : "debug"}
        with open(f'{pathToSave()}/save.json', 'w', encoding='utf-8') as file:
            json.dump(gameManager, file)
            print('Données éffacées ! Le jeu se ferme...')
            time.sleep(1)
            os.system("p")
    else: 
        print('Erreur de vérification, réessayez.')
        EndScreen(turn, gameManager, p1, p2, p)

def EndScreen(turn, gameManager, p1, p2, p):
    p1stats = gameManager[str(p1)]
    
    p2stats = gameManager[str(p2)]
    tprint('Game over')
    if turn == 11:
        p1stats[2] = p1stats[2] + 1
        p2stats[2] = p2stats[2] + 1
        cprint('Match nul, bien joué à tous les deux !', 'yellow')
    elif p == p1:
        p1stats[0] = p1stats[0] + 1
        p2stats[1] = p2stats[1] + 1
        print(colored(f"Félicitation {p}, tu as gagné ! ", 'yellow'))
    elif p == p2:
        p1stats[1] = p1stats[1] + 1
        p2stats[0] = p2stats[0] + 1
        print(colored(f"Félicitation {p}, tu as gagné ! ", 'yellow'))
    
    gameManager[p1] = p1stats
    gameManager[p2] = p2stats

    with open(f'{pathToSave()}/save.json', 'w', encoding='utf-8') as file:
        json.dump(gameManager, file)

    print(colored(f"\nSTATS :\n", 'red'))   
    print(f"{p1} : {p1stats[0]} victoires, {p1stats[1]} défaites, {p1stats[2]} matchs nuls   ")
    print(f"{p2} : {p2stats[0]} victoires, {p2stats[1]} défaites, {p2stats[2]} matchs nuls   ")
    print("\nVoulez vous rejouer ?")
    print("1) Quitter le jeu")
    print("2) Rejouer")
    print("3) Changer de joueurs") 
    print("4) Paramètres") 

    def endGameChoice() -> str:
        choice = input("")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            return choice
        else:
            return endGameChoice()
    mode = int(endGameChoice())
    if mode == 1:
        quit()
    elif mode == 2:
        setGame([], gameManager)

    elif mode ==3 :
        os.system(commands[sys][0])
        players = []
        temp = getPlayers(pathToSave())
        for p in temp.keys():
            players.append(p)
        setGame(players, gameManager)
    
    elif mode == 4:
        os.system(commands[sys][0])
        tprint('Settings')
        print("\nQue voulez-vous faire ?")
        print("1) Effacer les sauvegardes")
        print("2) Changer de Langue - pas encore disponible") 
        print("3) Retour") 

        def endGameChoice() -> str:
            choice = input("")
            if choice == "1" or choice == "2" or choice == "3" or choice == "4":
                return choice
            else:
                return endGameChoice()
        mode = int(endGameChoice())
        if mode == 1:
            eraseDatas(turn, gameManager, p1, p2, p)
        if mode == 2:
            pass

def isFirst():
    try:
        with open(pathToSave()+"/save.json", "r"):
            pass
    except FileNotFoundError:
        tprint('First use, initializing filesystem...')
        try:
            os.mkdir(pathToSave())
        except FileExistsError:
            pass
        save = open(pathToSave()+'/save.json', "w")
        debugDatas = {"#509 troubleshooting": "debug"}
        json.dump(debugDatas, save)
        save.close()



if __name__ == "__main__":

    isFirst()
    os.chdir(pathToScript)
    loading(__version__, pathToScript, pathToSave())
    os.system(commands[sys][0])
    #pathToScript = os.path.dirname(os.path.abspath(__file__))
    #print(pathToScript)
    gameManager = getPlayers(pathToSave())
    os.chdir(pathToScript)
    setGame(joueurs, gameManager)
    
