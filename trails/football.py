class Football:
    def __init__(self, name , TeamColor):
        self.name= name
        self.TeamColor= TeamColor
    
    def show_info(self):
        return f"name:{self.name}/n color:{self.TeamColor}"
    
class Sologun(Football):
    