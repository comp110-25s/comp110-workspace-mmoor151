"""File to define Bear class."""

__author__ = "730765813"


class Bear:
    """Define bear class."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Allow for the creation of multiple bear nodes."""
        self.age: int = 0
        self.hunger_score: int = 0

    def one_day(self) -> None:
        """How one day impacts a bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """The bear eats a fish."""
        self.hunger_score += num_fish
