import re

class Luhn:
    def __init__(self, card_num):
        
        self.card_num = card_num
        pass

    def checker(self, verified_string): 
  
        regex = re.compile(r'[^\d\s]') 

        if (regex.search(verified_string) == None) and (len(verified_string) > 1 and verified_string != ' 0') : 
            return True
        else: 
            return False 
    
    def valid(self):
       
        if self.checker(self.card_num) == True:

            card_digits = re.findall(r"\d+", self.card_num)
            
            clear_numbers = "".join(card_digits)

            output = str()
            n = 2
            for i,x in enumerate(reversed(clear_numbers)):
                if i % n == 0:
                    output = output + x
                else:
                    if (int(x) * 2) > 9:
                        output = output + str(int(x) * 2 - 9)
                    else:
                        output = output + str(int(x) * 2)
            
            final_number = sum(int(x) for x in output if x.isdigit())

            if final_number % 10 == 0:
                return True
            else:
                return False

        elif self.checker(self.card_num) == False:
            return False
        else: 
            return False
        pass
