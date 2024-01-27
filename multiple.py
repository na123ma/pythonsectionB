class add:
    @staticmethod
    def add2(a,b):
        return a+b
    @staticmethod
    def add3(a,b,c):
        return a+b+c
class sub:
    @staticmethod
    def sub2(a,b):
        return a-b
class mul:
    @staticmethod
    def mul1(a,b):
        return a*b
class cal(add,sub,mul):
    pass
obj=cal()
print(obj.add2(3,4))
print(obj.add3(8,5,6))
print(obj.mul1(5,4))
print(obj.sub2(5,3))