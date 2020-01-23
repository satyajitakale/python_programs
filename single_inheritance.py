class stud:
    def __init__(self,name,prof):
        self.name=name
        self.prof=prof
        
    def asch(self):
        print("I am in stud class\n")
    def stud_d(self):
        print(f"Name:{self.name}.\ni am a {self.prof}\n")

class tpo_stud(stud):
    def __init__(self):
        pass
    def tpo_stud_d(self,s):
        print(f"Name:{self.name}.\ni am a{self.prof} and {s} is a tpo student!!\n")
    def asch2(self):
        print("I am in tpo_stud_class\n")
sat=stud("sat","programmer")
sattya=tpo_stud()
sat.stud_d()
sattya.asch()
sattya.asch2()
