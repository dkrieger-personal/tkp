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
    if len(guess)!= 1:
        return ""
    if guess.isalpha():
        return guess.lower()
    return ""

def newindex (character):
    return ord(character)-97

def numnonzero (mylist):
    g=0
    for i in range(0,len(mylist)):
        if mylist[i]>0:
            g=g+1
    return g



#choose a word (display length, initialize game)
ThisGameWord = getword()
#print(ThisGameWord, len(ThisGameWord))
print('Your word has this many letters: ',len(ThisGameWord))

#guess a letter and put it in a variable
MyGuess = [] #array of guesses
youwin = 0 #indicates if you have won

a_val = ord('a')
for k in range (a_val,a_val+26):
    MyGuess.append(0)
    # print (k,a_val,MyGuess[k-a_val],chr(k))


while numnonzero(MyGuess)<3:
    currentguess=getguess()
    if currentguess=="":
        print ("Guesses must be single letters between a and z")
        continue
    gotit = 0
    if (MyGuess[newindex(currentguess)]>0):
        print ("You already guessed that")
    else:
        MyGuess[newindex(currentguess)] = 1
        for i in range (0,(len(ThisGameWord))):
            if (currentguess==ThisGameWord[i]):
                if gotit == 0:
                    print ("Yes, new correct letter!")
                    gotit=1
        if gotit == 0:
            print ("Sorry, that letter is incorrect")

    correctcount = 0
    for i in range (0,(len(ThisGameWord))):
        if (MyGuess[newindex(ThisGameWord[i])])>0:
            print(ThisGameWord[i],end='')
            correctcount+=1
        else:
            print('-',end='')

    print('')
    if correctcount == len(ThisGameWord):
        print('You win!')
        break


#insert the correctly guessed letters
#count the incorrect guesses until it has exceeded its maximum
#continue guessing and repeat



#for i in range(1,5):
#    print ('Guess #',i,':',getguess())


