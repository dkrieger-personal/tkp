import random
print("hangman!")
#choose a word (display length)
#guess a letter
#determine whether it's right or wrong
#insert the correctly guessed letters
#count tbe incorrect guesses until it has exceeded its maximum
#continue guessing and repeat
def getword ():
    words= ["green", "yellow", "chicken","gentlemen"]
    i=random.randint (0,len(words)-1)
    return words[i]

def getguess ():
    guess= input('guess-->')
    return guess

#choose a word (display length, initialize game)
ThisGameWord = getword()
#print(ThisGameWord, len(ThisGameWord))
print('Your word has this many letters: ',len(ThisGameWord))

#guess a letter and put it in a variable
MyGuess = [] #array of guesses
youwin = 0 #indicates if you have won
g=0 #counter of guesses
while youwin == 0:
    MyGuess.append(getguess())

    correctcount=0
    for i in range (0,(len(ThisGameWord))):
        gotit = 0
        for j in range(0,g+1):
            if (ThisGameWord[i]==MyGuess[j]):
                gotit=1
                correctcount+=1
        if (gotit==1):
            print(ThisGameWord[i],end='')
        else:
            print('-',end='')

    print('')
    if correctcount == len(ThisGameWord):
        print('You win!')
        youwin=1
    else:
        g+=1


#insert the correctly guessed letters
#count the incorrect guesses until it has exceeded its maximum
#continue guessing and repeat



#for i in range(1,5):
#    print ('Guess #',i,':',getguess())


