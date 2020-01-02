allergies = {
    1: 'eggs', #binary number 1
    2: 'peanuts', #binary number 10
    4: 'shellfish', #binary number 100
    8: 'strawberries', #binary number 1000
    16: 'tomatoes', #binary number 10000
    32: 'chocolate', #binary number 100000
    64: 'pollen', #binary number 1000000
    128: 'cats' #binary number 10000000
}

class Allergies(object):
    def __init__(self, score):
        """Calculates allergies for given score."""
        self.score = score
        self.lst = []
        self.__calculate_allergies()

    def __calculate_allergies(self):
        value = 1
        binary = "{:b}".format(self.score).zfill(8)

        for i in binary[::-1]:
            if value >= 256:
                break
            if i == '1':
                self.lst.append(allergies[value])
            value <<= 1

    def allergic_to(self, food):
        """Check if person is allergic on given food."""
        return food in self.lst
