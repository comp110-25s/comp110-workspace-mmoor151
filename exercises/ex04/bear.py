"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self, age: int, hunger_score: int):
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        self.age += 1
        self.hunger_score = max(0, self.hunger_score - 1)
        return None

    def eat(self, num_fish: int):
        if self.hunger_score > 0:
            self.hunger_score += num_fish
        else:
            print("The bear is not hungry!")
