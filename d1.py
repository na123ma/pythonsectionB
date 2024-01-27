class circle:
    def __init__(self,radious):
        self.radious=radious
    def __str__(self):
       return str(self.a)
    def area(self):
              area=3.14*self.radious**2
              return area
    def circum(self):
              a=2*3.14*self.radious
              return a
    def diameter(self):
              d=2*self.radious
              return d
    def incriment(self,step=1):
             self.a=self.a+step
             return self.a
    def decriment(self,step=1):
             self.a=self.a-step
             return self.a
s1=circle(5)