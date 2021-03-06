from lib.utils import *
import numpy as np
import sys, os.path

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

            if not os.path.isfile(self.dictFile):
                print("File not found: {}\n".format(self.dictFile))
                exit(0)
            #todo : check if file exists, add .txt if not provided
        else:
            print("-d is missing")
            self.help()
            exit(0)

        if self.utils.argHasValue("-m"):
            self.mask = self.utils.argValue("-m")
            for letter in self.mask:
                if letter not in "abcdefghijklmnopqrstuvwxyz.*?":
                    print("Invalid mask\n")
                    exit(0)
        else:
            print("-m is missing")
            self.help()
            exit(0)

        self.forbiddenLetter=""
        if self.utils.argHasValue("-f"):
            self.forbiddenLetter = self.utils.argValue("-f")

    def help(self):
        print()
        print("Usage: python hangmanfinder.py -d file -m mask [-f letters]")
        print("                               [[-h] | [-help] | [-?]]")
        print()
        print("Options:")
        print("   -d file     txt file to use as dictionary.")
        print("   -m mask     The mask to use, where * is a unknown letter.")
        print("               You can use \"*\", or \"?\" or \".\" for an unknown letter.")
        print("   -f letters  Results with one of these letters will be excluded.")
        print("   -h|help|?   (Optional) Print this help.")

    def validMask(self, word):
        if len(word) != len(self.mask):
            return False

        for letterMask, letterWord in zip(self.mask, word):
            if letterMask in ".*?":
                if letterWord in self.mask: #this letter was already found and is somewhere else in the word
                    return False
            else:
                if letterMask != letterWord:
                    return False

        return True

    def validWord(self, word):
        word=word.lower()
        if not self.validMask(word): #doesn't match to the mask
            return False

        for letter in word: #contains a forbidden letter
            if letter in self.forbiddenLetter:
                return False

        return True

    def computeValidWords(self):
        validWords=[]
        for word in self.dict:
            if self.validWord(word):
                validWords.append(word)

        return validWords

    def printNextLetter(self):
        apparitions={}
        for word in self.validWords:
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if letter in word and letter not in self.mask:
                    try:
                        apparitions[letter]=apparitions[letter]+1
                    except:#new letter
                        apparitions[letter]=1

        result=""
        maxVal = max(apparitions.values())
        if maxVal == len(self.validWords): #drop the maxVal
            tmp={}
            for key, value in apparitions.items():
                if value!=maxVal: 
                    tmp[key]=value
            apparitions = tmp.copy()
            maxVal = max(apparitions.values())

        topLetters = [letter for letter, val in apparitions.items() if val == maxVal]

        print("\nYou can ask for: {}".format(topLetters[0]), end="")
        for letter in topLetters[1:]:
            print(", {}".format(letter), end="")
        print("")

    def printwords(self):
        print("{}".format(self.validWords[0]), end="")
        for word in self.validWords[1:]:
            print(", {}".format(word), end="")
        print()

    def run(self):
        ##Reading the file
        print("Reading dict... ", end="")
        self.dict = np.genfromtxt(self.dictFile, dtype='str')
        print("Done")
        print("{} words found in dictionary".format(len(self.dict)))

        print("\nApplying mask \"{}\" ...".format(self.mask))
        self.validWords = self.computeValidWords()

        if len(self.validWords)==0:
            print("\nNO CORRESPONDING WORDS FOUND\n")

        elif len(self.validWords)==1:
            print("\nUNIQUE WORDS FOUND:")
            print(self.validWords[0])
            print()

        else:
            print("\n{} corresponding words found:  ".format(len(self.validWords)))
            self.printwords()
            print("{} corresponding words found:  ".format(len(self.validWords)))

            self.printNextLetter()
            print("{} tries left.\n".format(11-len(self.forbiddenLetter)))


if __name__ == '__main__':
    prog = hangmanFinder(sys.argv)
    prog.run()