import re

def recite(start_verse, end_verse):
    # "On the twelfth day of Christmas my true love gave to me: "
    #       "twelve Drummers Drumming, "
    #        "eleven Pipers Piping, "
    #        "ten Lords-a-Leaping, "
    #        "nine Ladies Dancing, "
    #        "eight Maids-a-Milking, "
    #        "seven Swans-a-Swimming, "
    #        "six Geese-a-Laying, "
    #        "five Gold Rings, "
    #        "four Calling Birds, "
    #        "three French Hens, "
    #        "two Turtle Doves, "
    #        "and a Partridge in a Pear Tree."
    song = {}
    song[0] = 'On the variable day of Christmas my true love gave to me: '
    song[1] = 'Partridge in a Pear Tree'
    song[2] = 'Turtle Doves'
    song[3] = 'French Hens'
    song[4] = 'Calling Birds'
    song[5] = 'Gold Rings'
    song[6] = 'Geese-a-Laying'
    song[7] = 'Swans-a-Swimming'
    song[8] = 'Maids-a-Milking'
    song[9] = 'Ladies Dancing'
    song[10] = 'Lords-a-Leaping'
    song[11] = 'Pipers Piping'
    song[12] = 'Drummers Drumming'

    numbers = {}
    numbers[0] = ''
    numbers[1] = 'a'
    numbers[2] = 'two'
    numbers[3] = 'three'
    numbers[4] = 'four'
    numbers[5] = 'five'
    numbers[6] = 'six'
    numbers[7] = 'seven'
    numbers[8] = 'eight'
    numbers[9] = 'nine'
    numbers[10] = 'ten'
    numbers[11] = 'eleven'
    numbers[12] = 'twelve'

    nth = {}
    nth[0] = ''
    nth[1] = 'first'
    nth[2] = 'second'
    nth[3] = 'third'
    nth[4] = 'fourth'
    nth[5] = 'fifth'
    nth[6] = 'sixth'
    nth[7] = 'seventh'
    nth[8] = 'eighth'
    nth[9] = 'ninth'
    nth[10] = 'tenth'
    nth[11] = 'eleventh'
    nth[12] = 'twelfth'

    for k, v in song.items():
        if k == end_verse:
            break
        elif k == 0:
            v = re.sub("variable", nth[end_verse], v)
        print(numbers[k] +" "+ v)
    print("######")
    pass
