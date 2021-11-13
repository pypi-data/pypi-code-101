#coding = utf-8
__version__ = '0.5.1'

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

global lang
lang = {}
with open(f"{pathToScript}/langues.json") as langages:
    lang = json.load(langages)

l= "en"

vars = variables()
colors = vars.colors
cases = vars.scheme
title = vars.title
commands = {"Windows": ["cls", "exit", "python -m Morpion"], 
            "Linux":["clear", "exit", """python3 -m Morpion"""],
            "Darwin": ["clear", "", """python3 -m Morpion"""] }

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
            
def getCoup(p, casesDispo, l) -> int:
    
    global lang
    coup = "test"
    while not str(coup) in str(casesDispo):
        isError = False
        coup = input(f'{p}, {lang[l][23]}  ?\n -> ')
        if coup == "":
            coup = "lol"
        try:
            coup = int(coup)
        except ValueError:
            isError = True
            print(lang[l][24])
            pass
        
        if not isError:
            print(lang[l][24])

    return coup 

def setGame(joueurs, gameManager, l):
    global lang
    for p in gameManager['currentPlayers']:
        joueurs.append(p)
    grid = setGrid(1, 0, 0, lang, l)
    os.system(commands[sys][0])
    for ligne in grid:
        print(ligne)
    game(joueurs, gameManager, l)

def game(joueurs, gameManager, l):

    global lang
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
        
        coup = getCoup(p, casesDispo, l)
        try:
            casesDispo.remove(coup)
        except ValueError:
            pass
        #print(casesDispo)
        
        if turn%2 == 1:
            newGrid = setGrid(turn, coup, Player1, lang, l)
        else:
            newGrid = setGrid(turn, coup, Player2, lang, l)
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
    EndScreen(turn, gameManager, p1, p2, p, True, l)

def eraseDatas(turn, gameManager, p1, p2, p, l):
    global lang
    captcha = str(uuid.uuid4())
    captcha = captcha[:5]
    print(lang[l][0] + captcha)
    
    a = input('-> ')
    if a == captcha:
        gameManager = {"# Error 509 TroubleShooter" : "debug"}
        with open(f'{pathToSave()}/save.json', 'w', encoding='utf-8') as file:
            json.dump(gameManager, file)
            print(lang[l][1])
            time.sleep(1)
        os.system(commands[sys][2])
    else: 
        print(lang[l][2])
        time.sleep(1)
        EndScreen(turn, gameManager, p1, p2, p, False,l)

def EndScreen(turn, gameManager, p1, p2, p, isEnd, l):

    global lang
    tprint('Game over')


    p1stats = gameManager[str(p1)]
    
    p2stats = gameManager[str(p2)]

    if turn == 11:
        if isEnd:
            p1stats[2] = p1stats[2] + 1
            p2stats[2] = p2stats[2] + 1
        cprint(lang[l][3], 'yellow')
    elif p == p1:
        if isEnd:
            p1stats[0] = p1stats[0] + 1
            p2stats[1] = p2stats[1] + 1
        print(colored(f"{lang[l][4]} {p}, {lang[l][5]} ! ", 'yellow'))
    elif p == p2:
        if isEnd:
            p1stats[1] = p1stats[1] + 1
            p2stats[0] = p2stats[0] + 1
        print(colored(f"{lang[l][4]} {p}, {lang[l][5]} ! ", 'yellow'))
    if isEnd:
        gameManager[p1] = p1stats
        gameManager[p2] = p2stats

        with open(f'{pathToSave()}/save.json', 'w', encoding='utf-8') as file:
            json.dump(gameManager, file)

    print(colored(f"\nSTATS :\n", 'red'))   
    print(f"{p1} : {p1stats[0]} {lang[l][6]}, {p1stats[1]} {lang[l][7]}, {p1stats[2]} {lang[l][8]}   ")
    print(f"{p2} : {p2stats[0]} {lang[l][6]}, {p2stats[1]} {lang[l][7]}, {p2stats[2]} {lang[l][8]}   ")
    print(f"\n{lang[l][9]}")
    print(f"1) {lang[l][10]}")
    print(f"2) {lang[l][11]}")
    print(f"3) {lang[l][12]}") 
    print(f"4) {lang[l][13]}") 

    def endGameChoice() -> str:
        choice = input("")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            return choice
        else:
            return endGameChoice()
    mode = int(endGameChoice())
    if mode == 1:
        os.system(commands[sys][0])
        tprint(lang[l][25])
        quit()
    elif mode == 2:
        setGame([], gameManager, l)

    elif mode ==3 :
        os.system(commands[sys][0])
        players = []
        temp = getPlayers(pathToSave(), lang , l)
        for p in temp.keys():
            players.append(p)
        setGame(players, gameManager, l)
    
    elif mode == 4:
        os.system(commands[sys][0])
        tprint(f'{lang[l][13]}')
        print(f"\n{lang[l][9]}")
        print(f"1) {lang[l][14]}")
        print(f"2) {lang[l][15]}") 
        print(f"3) {lang[l][16]}") 

        def endGameChoice() -> str:
            choice = input("")
            if choice == "1" or choice == "2" or choice == "3" or choice == "4":
                return choice
            else:
                return endGameChoice()
        mode = int(endGameChoice())
        if mode == 1:
            eraseDatas(turn, gameManager, p1, p2, p, l)
        elif mode == 2:
            setLang(turn, gameManager, p1, p2, p, True, l)
        else:
            EndScreen(turn, gameManager, p1, p2, p, False, l)

def setLang(turn, gameManager, p1, p2, p, isEnd, l):
    os.system(commands[sys][0])
    tprint('language selection')
    print('1) English (default)')
    print('2) Français')
    print(f"3) {lang[l][16]}")
    print("Note that if your selection doesn't exist, the language will be set on English.")

    entry = input('\n-> ')
    


    if entry == "2":
        entry = 'fr'
        l = 'fr'
        with open(pathToSave()+"/langage.txt", "w") as output:
            output.write('fr')

    elif entry == "3":
        pass
    else: 
        entry == 'en'
        l = 'en'
        with open(pathToSave()+"/langage.txt", "w") as output:
            output.write('en')
    
    if isEnd == True:
        print(l)
        EndScreen(turn, gameManager, p1, p2, p, False, l)

def isFirst():

    global lang
    try:
        with open(pathToSave()+"/langage.txt", "r"):
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

        langage = open(pathToSave()+"/langage.txt", "w")
        os.system(commands[sys][0])
        langage.write('en')
        langage.close()
        setLang(None, None, None, None, None, False, l)

if __name__ == "__main__":

    isFirst()

    with open(pathToSave()+"/langage.txt", "r") as currentLang:
        l = currentLang.read()

    os.chdir(pathToScript)
    loading(__version__, pathToScript, pathToSave(), lang, l)
    os.system(commands[sys][0])
    #pathToScript = os.path.dirname(os.path.abspath(__file__))
    #print(pathToScript)
    gameManager = getPlayers(pathToSave(), lang, l)
    os.chdir(pathToScript)
    setGame(joueurs, gameManager, l)
