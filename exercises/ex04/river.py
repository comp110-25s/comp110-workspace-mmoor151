__author__ = "730765813"

"""File to define River class."""

from ex04.fish import Fish
from ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = [Fish() for _ in range(num_fish)]
        self.bears: list[Bear] = [Bear() for _ in range(num_bears)]

    def view_river(self) -> None:
        """Print what's happening in the river"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self) -> None:
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulate one week of life in the river"""
        for _ in range(7):
            self.one_river_day()

    def check_ages(self) -> None:
        """Checks how old the animals are and if they die of old age"""
        surviving_fish = [fish for fish in self.fish if fish.age <= 3]
        surviving_bears = [bear for bear in self.bears if bear.age <= 5]
        self.fish = surviving_fish
        self.bears = surviving_bears

    def remove_fish(self, amount: int) -> None:
        """A fish is removed from the river"""
        self.fish = self.fish[amount:]

    def bears_eating(self) -> None:
        """Bears eat fish"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)

    def check_hunger(self) -> None:
        """How hungry are the bears and will they starve"""
        surviving_bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = surviving_bears

    def repopulate_fish(self) -> None:
        """Fish reproduction"""
        num_new_fish = (len(self.fish) // 2) * 4
        if len(self.fish) > 2:
            for _ in range(num_new_fish):
                self.fish.append(Fish())

    def repopulate_bears(self) -> None:
        """Bear reproduction"""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())
