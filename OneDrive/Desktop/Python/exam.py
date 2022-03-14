class Employees:

    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}' .format(self.first, self.last)