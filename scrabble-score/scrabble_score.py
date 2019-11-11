import random
import operator

def score(word):
    print("welcome to the letter game challenge")
    response=input("enter a word:\n")
    print(format(response)) # prints the word you have entered

    letterpoints = { "E":(1),
                     "A":(2),
                     "R":(3),
                     "I":(4),#values for each number as shown "i" = 4
                     "O":(5),
                     "T":(6),
                     "N":(7),
                     "S":(8),# values for each number again "s" = 4
                     "L":(9),
                     "C":(10),
                     "U":(11),
                     "D":(12),
                     "P":(13),
                     "M":(14),
                     "H":(15),
                     "G":(16),
                     "B":(17),
                     "F":(18),
                     "Y":(19),
                     "W":(20),
                     "K":(21),
                     "V":(22),
                     "X":(23),
                     "Z":(24),
                     "J":(25),
                     "Q":(26),
    }

    response = response.upper()
    total = 0
    for letter in response:
        total += letterpoints.get(letter)

    print('your score is {}'.format(total))

    pass
