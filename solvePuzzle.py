#INPUT: string of 7 letters
#First letter is the center required letter

from operator import contains
import sys

def main(letters):
    solutions = []
    args = list(letters[0])
    first = args[0]
    with open("validwords.txt") as words:
        print("success")
        for word in words:
            word = word.strip()
            #Check for required letter
            if first in word:
                flag = False
                for letter in word:
                    if not letter in args:
                        flag = True
                        break
                if not flag:
                    solutions.append(word)


    print(solutions)

if __name__ == __name__:
    main(sys.argv[1:])