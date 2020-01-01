from collections import Counter
def find_anagrams(word, candidates): return [item for item in candidates if sorted(item.lower()) == sorted(word.lower()) and item.lower() != word.lower()]
