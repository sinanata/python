class School:
    def __init__(self):

        self.student_dict = {}

        pass

    def add_student(self, name, grade):

        self.student_dict.__setitem__(name, grade)

        pass

    def roster(self):

        return [k for k in self.student_dict.keys()]

        pass

    def grade(self, grade_number):

        output = []

        list_of_keys = [key for (key, value) in self.student_dict.items() if value == grade_number]

        return list_of_keys

        pass
