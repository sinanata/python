import re

def is_isogram(string):
    x = []
    cstring = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?, ]", "", string)
    for i in cstring.lower():
        if i in x:
            return False
        else:
            x.append(i)
    return True