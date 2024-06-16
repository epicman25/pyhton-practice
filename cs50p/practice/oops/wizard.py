class Wizard:
    def __init__(self,name) -> None:
        self.name = name
        
        
class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house
        
class Professor(Wizard):

    
    def __init__(self,name,subject):
        super().__init__(name)
    
        self.subject = subject
        
        
wizard = Wizard("iuasfd")
student = Student("harry","TT")
professor = Professor("Sev","gg")