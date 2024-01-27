class Mtca:
    chairman='Mr. sunil'
    location='palamaner'
    college = 'Mtca'
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mca(Mtca):
    principal='Mr. prabhakar naidu'
    strenth = 240
    staff = 9
class Btech(Mtca):
    principal = 'Ms. Sravani'
    strength = 350
    staff = 35
raj=Mca('raj',7645973209)
siva=Btech('siva',37261476145)