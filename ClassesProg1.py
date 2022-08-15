# Classes demo program

class employee:
    def __init__(self, firstName, lastName, pay):
        self.fn = firstName
        self.ln = lastName
        self.pay = pay
        self.email = firstName + "." + lastName + "@gmail.com"


emp1 = employee("archana", "raghupathy", 200000)
print(emp1.fn, emp1.ln, emp1.pay, emp1.email)
