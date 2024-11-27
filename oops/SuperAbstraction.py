from abc import ABC, abstractmethod


class Superhero(ABC):
    
    @abstractmethod
    def fight_crime(self):
        pass

    @abstractmethod
    def use_power(self):
        pass


class Superman(Superhero):
    
    def fight_crime(self):
        return "Superman is fighting crime with super strength!"
    
    def use_power(self):
        return "Superman uses his laser vision!"


class Batman(Superhero):
    
    def fight_crime(self):
        return "Batman is fighting crime with martial arts and gadgets!"
    
    def use_power(self):
        return "Batman uses his Batmobile to chase criminals!"


superman = Superman()
batman = Batman()


print(superman.fight_crime())  
print(superman.use_power())    

print(batman.fight_crime())    
print(batman.use_power())     
