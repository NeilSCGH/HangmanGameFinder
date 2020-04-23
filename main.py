import pandas as pd
import numpy as np


##Reading the file
print("Getting data\n")
dict = np.genfromtxt('dict2.txt',dtype='str')

##Constraint
unAllowedLetters = "cdlnu"
mask = "*a*ier"

def validMask(word):
    if len(word)!=len(mask):
        return False

    for i in range(len(word)):
        letterMask=mask[i]
        letterWord=word[i]
        if letterMask != "*" and letterMask!=letterWord:
            return False

    return True

def validWord(word):
    word=word.lower()
    if not validMask(word):
        return False

    for letter in word:
        if letter in unAllowedLetters:
            return False

    return True


possibilities=[]
for word in dict:
    if validWord(word):
        possibilities.append(word)


print(possibilities)
print("\nmodel:",mask)
print("from {} to {}".format(len(dict),len(possibilities)))