from lib.utils import *
import numpy as np
import sys

class hangmanFinder():
    def __init__(self, args):
        self.utils = utils(args)
        self.setup(args)#process the arguments

    def setup(self, args):
        if self.utils.argExist("-h") or self.utils.argExist("-help") or self.utils.argExist("-?"):
            self.help()
            exit(0)

        if self.utils.argHasValue("-d"):
            self.dictFile = self.utils.argValue("-d")
            #todo : check if file exists, add .txt if not provided
        else:
            print("-d is missing")
            self.help()
            exit(0)

        if self.utils.argHasValue("-m"):
            self.mask = self.utils.argValue("-m")
        else:
            print("-m is missing")
            self.help()
            exit(0)

        self.forbiddenLetter=""
        if self.utils.argHasValue("-f"):
            self.forbiddenLetter = self.utils.argValue("-f")

    def help(self):
        print()
        print("Usage: python main.py -d file -m mask [-f letters]")
        print("                      [[-h] | [-help] | [-?]]")
        print()
        print("Options:")
        print("   -d file     txt file to use as dictionary.")
        print("   -m mask     The mask to use, where * is a unknown letter.")
        print("   -f letters  Results with one of these letters will be excluded.")
        print("   -h|help|?   (Optional) Print this help.")

    def validMask(self, word):
        if len(word)!=len(self.mask):
            return False

        for i in range(len(word)):
            letterMask=self.mask[i]
            letterWord=word[i]
            if letterMask == "*":
                if letterWord in self.mask:
                    return False
            else:
                if letterMask!=letterWord:
                    return False

        return True

    def validWord(self, word):
        word=word.lower()
        if not self.validMask(word):
            return False

        for letter in word:
            if letter in self.forbiddenLetter:
                return False

        return True

    def computeValidWords(self):
        validWords=[]
        for word in self.dict:
            if self.validWord(word):
                validWords.append(word)

        return validWords

    def run(self):
        ##Reading the file
        print("Reading dict...", end="")
        self.dict = np.genfromtxt(self.dictFile, dtype='str')
        print("Done")
        print("{} words found in dictionary".format(len(self.dict)))

        print("\nApplying mask \"{}\" ...".format(self.mask),end="")
        self.validWords = self.computeValidWords()
        print("Done")

        print("{} corresponding words found:\n".format(len(self.validWords)))
        #print("Excluding letters :",self.forbiddenLetter)
        print(self.validWords)


        proba={}
        for word in self.validWords:
            for letter in word:
                if letter not in self.mask:
                    try:
                        proba[letter]=proba[letter]+1
                    except:
                        proba[letter]=1

        maxLetter=max(proba, key=proba.get)
        print("\nNext letter to ask for is {}\n".format(maxLetter))


if __name__ == '__main__':
    prog = hangmanFinder(sys.argv)
    prog.run()