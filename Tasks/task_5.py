class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def number_of_wins(self):
        return f"Футбольных побед: {self.victories}"

    def number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Футбольных поражений: {self.losses}"

    def total_points(self):
        number_of_points = 3 * self.victories + self.draws
        return number_of_points

class Hockey(Results):
    def number_of_wins(self):
        return f"Футбольных побед: {self.victories}"

    def number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Футбольных поражений: {self.losses}"

    def total_points(self):
        number_of_points = 2 * self.victories + self.draws
        return number_of_points

football_team = Football(2,2,2)
hockey_team = Hockey(2,2,2)

for team in (football_team, hockey_team):
    for method_name in dir(team):
        if callable(getattr(team, method_name)) and not method_name.startswith("__"):
            print(getattr(team, method_name)())
