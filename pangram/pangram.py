import string
def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) >= alphabet
