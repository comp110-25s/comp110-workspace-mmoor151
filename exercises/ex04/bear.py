__author__ = "730765813"

"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        """Allow for the creation of multiple bear nodes"""
        self.age: int = 0
        self.hunger_score: int = 0

    def one_day(self) -> None:
        """How one day impacts a bear"""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """The bear eats a fish"""
        self.hunger_score += num_fish
