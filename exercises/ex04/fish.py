"""File to define Fish class."""

__author__ = "730765813"


class Fish:
    """Define fish class."""

    age: int

    def __init__(self) -> None:
        """Allow for the creation of multiple fish nodes."""
        self.age: int = 0

    def one_day(self) -> None:
        """How one day impacts a fish."""
        self.age += 1
