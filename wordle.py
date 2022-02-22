from calendar import c
import random

#holds the entire game screen

#list of all possible words
wordList = []
gameScreen = None
word = ""

#current slots 
currentSlot = 0

#file of all words
chosenFile = "No File"

#word that is correct
curCorrectWord = ""
def initGame():
    global wordLength
    wordLength = int(input("How many letters do you want the word to be? "))
    global xDimension
    global yDimension
    xDimension = wordLength
    yDimension = wordLength + 1
    global gameScreen
    gameScreen = [[0 for x in range(xDimension)] for y in range(yDimension)] 
    if wordLength == 3:
        return "wordsThree.txt"
    elif wordLength == 4:
        return "wordsFour.txt"
    elif wordLength == 5:
        return "wordsFive.txt"
    elif wordLength == 6:
        return "wordsSix.txt"
    elif wordLength == 7:
        return "wordsSeven.txt"
    else:
        print("Not a valid number (3-7)")

def getUserWord():
    correctInputLength = False
    inWordList = False
    global word 
    word = input("Give a " + str(wordLength) + " letter word: ")
    if len(word) == wordLength:
        correctInputLength = True
    else:
        print("Your input is not the right amount of letters")
        getUserWord()
    if word in wordList:
        inWordList = True
    else:
        print("Your input is not a valid word in wordlist")
        getUserWord()
    return True
    
def getGameScreen(inputWord, curCorrectWord):

    for i in range(xDimension):
        coverPicked = False
        #print(inputWord)
        if inputWord[i] == curCorrectWord[i]:
            #print('right alignment')
            gameScreen[currentSlot][i] = "{" + inputWord[i] + "}"
            coverPicked = True
        if inputWord[i] != curCorrectWord[i] and coverPicked == False: 
                for j in range(xDimension):
                    #print("check letter in word")
                    if inputWord[i] == curCorrectWord[j] and coverPicked == False:
                        #print("letter in word")
                        gameScreen[currentSlot][i] = "(" + inputWord[i] + ")"
                        coverPicked = True
        if coverPicked == False:
            #print("neither")
            gameScreen[currentSlot][i] = "[" + inputWord[i] + "]"

def printScreen():
    screen = ""
    for i in range(yDimension):
        if i != 0:
            screen += "\n"
        for j in range(xDimension):
            if str(gameScreen[i][j]) == "0":
                screen += "[ ]"
            else:
                screen += str(gameScreen[i][j])
    print(screen)

chosenFile = initGame()
try:
    f = open(chosenFile, "r")
    lineCount = 0
    for line in f:
        if line != "\n":
            lineCount += 1
    f.close()
    f = open(chosenFile, "r")
    for i in range(lineCount):
        a = f.readline().lower()
        wordList.append(a.strip())
    f.close()
except:
    print("Game screen not chosen")
    initGame()

#choose correct word
curCorrectWord = wordList[random.randint(0, len(wordList)-1)]

for i in range(yDimension):
    getUserWord()
    getGameScreen(word, curCorrectWord)
    printScreen()
    currentSlot += 1
    if word == curCorrectWord:
        print("""
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
Stats:
Word = {}
Tries = {}
        """.format(curCorrectWord, currentSlot))
        break
    elif currentSlot == yDimension:
        print("""
██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝██║
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░██║
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝╚═╝
Stats:
Word = {}
Tries = {}
""".format(curCorrectWord, currentSlot))
        break



