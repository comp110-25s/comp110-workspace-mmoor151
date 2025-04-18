__author__ = "730765813"

"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        """Allow for the creation of multiple fish nodes"""
        self.age = 0

    def one_day(self) -> None:
        """How one day impacts a fish"""
        self.age += 1
