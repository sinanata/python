from re import sub

def encode(string):
    return sub(r'(.)\1*', lambda s: str( len(s.group(0)) if len(s.group(0)) > 1 else '' ) + s.group(1),
               string)

def decode(string):
    return sub(r'(\d+)(\D)', lambda s: s.group(2) * int(s.group(1)),
               string)
