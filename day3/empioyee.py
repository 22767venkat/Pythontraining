class Employee:
    def __init__(self,fname,lname,city):
        self.firstname=fname
        self.lastname=lname
        self.city=city

    def getName(self):
         return self.firstname[0]+self.lastname[0]+self.city[0]

emp = Employee("Venkat", "Thota", "Guntur")
name=emp.getName();
print(name.upper())


