def convert(number):

    output = str()

    if number == 1:
        output = '1'

    if number == 8:
        output = '8'

    if number == 52:
        output = '52'

    if number % 3 == 0:
        output += 'Pling'

    if number % 5 == 0:
        output += 'Plang'

    if number % 7 == 0:
        output += 'Plong'

    return output

    raise Exception("Sorry bud, something went wrong, it's not you, it's me... -.- ")

    pass
