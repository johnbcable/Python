class Payroll:
    def __init__(self, name):
        self.name = name
        self.hours = 0
        self.overHours = 0
        self.wage = 0
    def setEarnings(self, wage):
        self.wage = wage
    def setHours(self,hours):
        self.hours = hours
    def setOvertime(self,hours = 0):
        self.overHours = hours
    def calculate(self):
        print(self.name , ' worked:')
        print(self.hours , ' normal hours @ ' , self.wage , ' for $' , self.hours * self.wage)
        print(self.overHours , ' overtime hours @ ' , self.wage * 1.5 , ' for $' , self.overHours * 1.5 * self.wage)
        print('Totalling: $' , ((self.wage*1.5*self.overHours)+ (self.wage*self.hours)) , ' for One Weeks work')
        
alex = Payroll('Alex')
alex.setEarnings(14.20)
alex.setHours(4.2)
alex.setOvertime(1)
alex.calculate()