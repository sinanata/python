STUDENT_LIST = ['Alice', 'Bob', 'Charlie', 'David', 'Eve',
        'Fred', 'Ginny', 'Harriet','Ileana', 'Joseph',
        'Kincaid', 'Larry']

PLANTS = {'V': 'Violets', 'C': 'Clover', 'R': 'Radishes', 'G': 'Grass'}

class Garden(object):
    def __init__(self, diagram, students=STUDENT_LIST):
        split_diagram = diagram.split('\n')
        self.row1 = split_diagram[0]
        self.row2 = split_diagram[1]
        self.students = students
        self.students.sort()

    def plants(self, student):
        n = self.students.index(student) * 2
        r1 = self.row1
        r2 = self.row2
        return [PLANTS[r1[n]], PLANTS[r1[n+1]], PLANTS[r2[n]], PLANTS[r2[n+1]]]
