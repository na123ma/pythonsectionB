class grandparent:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)
class parent(grandparent):
   def __init__(self,e,f,c,d):
       super().__init__(c,d)
       self.e=e
       self.f=f
   def display(self):
       super().display()
       print(self.e,self.f)
class child(parent):
    def __init__(self,c,d,e,f,g,h):
        super().__init__(c,d,e,f)
        self.g=g
        self.h=h
    def display(self):
       super().display()
       print(self.g,self.h)
obj=child(30,40,50,80,90,60)