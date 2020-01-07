def slices(series, length):
    return list(split_by_n(series,length))

def split_by_n( seq, n ):
    seq = str(seq)
    while seq and len(seq[:n]) == n:
        try:
            yield str(seq[:n])
            seq = seq[1:]
        except:
            pass
