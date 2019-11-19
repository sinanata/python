class School:
    def __init__(self):
        self.student_dict = {}
        pass

    def add_student(self, name, grade):
        self.student_dict.__setitem__(name, grade)
        pass

    def roster(self):
        return [i[0] for i in sorted(sorted(self.student_dict.items(), key=lambda x:x[0]), key=lambda x:x[1])]
        pass

    def grade(self, grade_number):
        list_of_keys = [key for (key, value) in sorted(self.student_dict.items(), key=lambda x:x[0]) if value == grade_number]
        return list_of_keys
        pass
