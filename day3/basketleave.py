from leave import Leave
class BasketOfLeave:
   def __init__(self,Employeeid,Name,LeaveBalance,ApplyingLeave):
        self.employeeid=Employeeid
        self.name=Name
        self.leavebalance=LeaveBalance
        self.applyingleave=ApplyingLeave
   def display(self):
        return self.employeeid,self.name,self.leavebalance,self.applyingleave