def distance(strand_a, strand_b):
    if (len(strand_a) == len(strand_b)):
        return sum ( strand_a[i] != strand_b[i] for i in range(len(strand_a)) )
    else:
        print("Something went wrong with these: ", strand_a, strand_b)
        raise ValueError("Something went wrong with these: ", strand_a, strand_b)