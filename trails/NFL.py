class NFLTeam:
    def __init__(self, name, city, division):
        self.name = name
        self.city = city
        self.division = division
        self.wins = 0
        self.losses = 0

    def record_game(self, result):
        if result.lower() == 'win':
            self.wins += 1
        elif result.lower() == 'loss':
            self.losses += 1
        else:
            print("Invalid result. Use 'win' or 'loss'.")

    def win_percentage(self):
        total_games = self.wins + self.losses
        if total_games == 0:
            return 0.0
        return self.wins / total_games * 100

    def display_team_info(self):
        print(f"Team: {self.city} {self.name}")
        print(f"Division: {self.division}")
        print(f"Record: {self.wins}-{self.losses} ({self.win_percentage():.2f}% wins)")

patriots = NFLTeam("Chiefs", "Kansas", "AFC West")
patriots.record_game("win")
patriots.record_game("win")
patriots.record_game("win")
patriots.display_team_info()

