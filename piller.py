class parent:
    a=20
    b=41

    def __init__(self,c,d):
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)

class child(parent):
    a=80

    def __init__(self,c,d,e,f):
        parent.__init__(self,c,d)
        self.e=e
        self.f=f
    def display(self):
        super().display()
        print(self.e,self.f)
obj = child(4,6,9,4)