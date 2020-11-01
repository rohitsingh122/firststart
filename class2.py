class Employee:
    no_of_leaves =8 #class variable
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
    def printdet(self):
        print("employee name:",self.name)
        print("employee salary:",self.salary)
        print("employee role:",self.role)
        
      

e =[ Employee("rohit",3444,"student"),
Employee("salim",3445,"worker"),Employee("radhe",34444,"engineer")]
for i in e:
    i.printdet()



