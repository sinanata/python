import re
def response(hey_bob):

    cleared = str(re.findall(r'\b[a-zA-Z]+\b', hey_bob))

    if cleared.isupper() == False and hey_bob.rstrip().endswith('?'):
        return 'Sure.'
    elif hey_bob.rstrip().endswith('?') and cleared.isupper() == True:
        return 'Calm down, I know what I\'m doing!'
    elif cleared.isupper() == True:
        return 'Whoa, chill out!'
    elif hey_bob.rstrip() == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
