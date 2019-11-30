rna = {"G": "C",
   "C": "G",
   "T": "A",
   "A": "U"
   }

def to_rna(dna_strand):
    res = ""

    for char in dna_strand:
        if char in rna:
            res += rna[char]
        else:
            res += char

    return res
