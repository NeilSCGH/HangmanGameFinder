# HagmanGameFinder

This program is made to cheat at the hangman game. 
It will lists all possible words, and give you the next letter to ask for.
```
Usage: python main.py -d file -m mask [-f letters]
                      [[-h] | [-help] | [-?]]

Options:
   -d file     txt file to use as dictionary.
   -m mask     The mask to use, where * is a unknown letter.
   -f letters  Results with one of these letters will be excluded.
   -h|help|?   (Optional) Print this help.
```

## Example
```
python main.py -d dict.txt -m "s**en*e" -f "ardpu"
```
 Will return
```
['science', 'silence']
...
Ask for c
```
