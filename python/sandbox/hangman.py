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

for i in range(0,10):
    print (getword())
    