class Matrix(object):
    def __init__(self, matrix_string):
        A = matrix_string.split('\n')
        rows = [list(map(int,a.split(' '))) for a in A]
        cols = list(map(list,zip(*rows)))
        self.row = lambda index:rows[index-1]
        self.column = lambda index:cols[index-1]
