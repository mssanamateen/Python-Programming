class Superhero:
    def __init__(self,name,power):
        self.name=name
        self.power=power

    def display_power(self):
        print(f"{self.name}'s power is {self.power}.")


class TechHero(Superhero):
    def __init__(self,name,power,suit_name):
        super().__init__(name,power)
        self.suit_name=suit_name

    def display_suit(self):
        print(f"{self.name} uses the {self.suit_name} suit.")


class TeamLeader(TechHero):
    def __init__(self, name,power,suit_name,team_name):
        super().__init__(name,power,suit_name)
        self.team_name=team_name

    def display_team(self):
        self.display_power()
        self.display_suit()
        print(f"{self.name} leads the superhero team '{self.team_name}'.")


ironman = TeamLeader("Iron Man", "Genius Intellect", "Mark 85", "Avengers")


        
ironman.display_team()        
