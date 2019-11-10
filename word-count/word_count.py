from collections import *
import re
def count_words(sentence):
    sentence = re.sub("_", " ", sentence.lower())
    inspected = re.findall(r"([\w]+[']?[\w]+|\d|[a-z])", sentence.lower())
    
    return Counter(inspected)
pass