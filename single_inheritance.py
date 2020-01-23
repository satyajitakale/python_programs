class stud:
    def __init__(self,name,prof):
        self.name=name
        self.prof=prof
        
    def stud_d(self):
        print(f"Name:{self.name}.\ni am a {self.prof}")

class tpo_stud(stud):
    def tpo_stud_d(self,s):
        print(f"Name:{self.name}.\ni am a{self.prof} and {s} is a tpo student!!")
sat=stud("sat","programmer")
sattya=tpo_stud("sattya","programmer")
sat.stud_d()
sattya.stud_d()
sattya.tpo_stud_d("satyam")
