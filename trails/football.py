class Football:
    def __init__(self, name , TeamColor, sologun):
        self.name= name
        self.TeamColor= TeamColor
        self.sologun= sologun
    
    def show_info(self):
        print(f"Team name:{self.name}\nSologun:{self.sologun}\nTeam Color:{self.TeamColor}")
    
class Uniform(Football):
    def __init__(self, name, TeamColor, sologun, size, weight, material):
        super().__init__(name, TeamColor, sologun)
        self.size= size
        self.weight= weight
        self.material= material
        
    def show_info(self):
        super().show_info()
        print(f"Size:{self.size}, Weight:{self.weight}, Material:{self.material}")
            
team1 = Uniform("Chelsea", "blue & white", "The pride of london", 5, 450, "Poly")
team1.show_info()
    