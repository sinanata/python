import re

def recite(start_verse, end_verse):


    Dictionary2D = {
    12:["twelfth", "twelve"],
    11:["eleventh", "eleven"],
    10:["tenth", "ten"],
    9:["ninth", "nine"],
    8:["eigth", "eigth"],
    7:["seventh", "seven"],
    6:["sixth", "six"],
    5:["fifth", "five"],
    4:["fourth", "four"],
    3:["third", "three","French Hens, "],
    2:["second", "two","Turtle Doves, "],
    1:["first", "and a", "Partridge in a Pear Tree."]
    }

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


    print("On the " + nth[end_verse] + " day of Christmas my true love gave to me: ")

    for k, v in song.items()[::-1]:
        if song[k] > 1
            print(numbers[k] +" "+ v)


    if end_verse > 1:
        end_line = "and"
        print(end_line + " " + numbers[1] + " " + "Partridge in a Pear Tree")
    else:
        print(numbers[1] + " " + "Partridge in a Pear Tree")

    print("######")
    pass
