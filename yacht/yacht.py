from collections import Counter

def YACHT(x):
    return 50 if len(set(x)) == 1 else 0

def ONES(x):
    return sum([i for i in x if i == 1])

def TWOS(x):
    return sum([i for i in x if i == 2])

def THREES(x):
    return sum([i for i in x if i == 3])

def FOURS(x):
    return sum([i for i in x if i == 4])

def FIVES(x):
    return sum([i for i in x if i == 5])

def SIXES(x):
    return sum([i for i in x if i == 6])

def FULL_HOUSE(x):
    return sum(x) if sorted(Counter(x).values()) == [2, 3] else 0

def FOUR_OF_A_KIND(x):
    four_times_elements = [dice for dice in set(x) if x.count(dice) >= 4]
    return 4*four_times_elements[0] if len(four_times_elements) == 1 else 0

def LITTLE_STRAIGHT(x):
    return 30 if sorted(x) == [1, 2, 3, 4, 5] else 0

def BIG_STRAIGHT(x):
    return 30 if sorted(x) == [2, 3, 4, 5, 6] else 0

def CHOICE(x):
    return sum(x)

def score(dice, category):
    return category(dice)
