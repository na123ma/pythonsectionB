from abc import ABC, abstractmethod
class Modelcar(ABC):
    @abstractmethod
    def Break():
        pass
    def Speed_up():
            pass
    def Speed_down():
          pass
    def Gear_change():
         pass
class Nexon(Modelcar):
           def __init__(self,speed=0,stop=True):
                 self.speed=speed
                 self.stop=stop
           def speed_up(self):
                 self.speed+=5
                 self.stop=False
                 print(f'accelerated by 5 km/hr and current speed is {self.speed}')
           def speed_down(self):
              if not self.stop:
                 self.speed-=5
                 if self.speed == 0:   
                    self.stop=True
                 print(f'accelerated by 5 km/h and current speed is {self.speed}')
           def gear_change(self,speed=0):
                if speed in range(5,11):
                     return '1st gear'
                elif speed in range(10,21):
                     return '2nd gear'
                elif speed in range(20,31):
                     return '3rd gear'
                elif speed in range(30,41):
                     return '4th gear'
                else:
                     return 'the car in reverse'
           def  Break(self):
                 self.speed=0
                 self.stop=True
