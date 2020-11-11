import numpy as np

##Reading the file
print("Getting data\n")
dict = np.genfromtxt('dict4.txt',dtype='str')

##Constraint
unAllowedLetters = ""
mask = "*****e*e*****e**"

def validMask(word):
    if len(word)!=len(mask):
        return False

    for i in range(len(word)):
        letterMask=mask[i]
        letterWord=word[i]
        if letterMask == "*":
            if letterWord in mask:
                return False
        else:
            if letterMask!=letterWord:
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
print("\nWords in dict:",len(dict))
print("None of:",unAllowedLetters)
print("Model:",mask)
print("Words left:",len(possibilities))


proba={}
for word in possibilities:
    for letter in word:
        if letter not in mask:
            try:
                proba[letter]=proba[letter]+1
            except:
                proba[letter]=1

maxLetter=max(proba, key=proba.get)
print("\nAsk for",maxLetter)
