class MTCA:
    principal='mr prabhakar naidu'
    college='mother theresa'
    location='palamaner'
    def __init__(self,name,mob,mailID,sem):
        self.student_name=name
        self.mobile=mob
        self.email_ID=mailID
        self.semister=sem
    def update_mob(self,new):
        self.mobile=new
        print('mobile number updated')
    @classmethod
    def change_college(cls,new):
        cls.college=new
    @staticmethod
    def add(a,b):
        return a+b
s1=MTCA('abc',1234,'abc@gmail.com','1stsem')
s2=MTCA('gbd',1431,'gbd@gmail.com','1stsem')