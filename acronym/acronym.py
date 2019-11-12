import re
def abbreviate(words):
    
    words = re.sub("_|-", " ", words)
    inspected = re.findall(r"([\w]+[']?[\w]+|\d|[a-zA-Z])", words)

    acronym = ''.join(word[0] for word in inspected)
    
    return acronym.upper()