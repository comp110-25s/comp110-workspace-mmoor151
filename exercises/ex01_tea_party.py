"""Quantity of tea bags, treats, and cost for a tea party based on guest numbers"""

__author__ = "730765813"


def main_planner(guests: int):
    """Displays the total number of tea bags, treats, and cost given guests"""
    print(str("A Cozy Tea Party for " + str(guests) + " People!"))
    print(str("Tea Bags: " + str(tea_bags(guests))))
    print(str("Treats: " + str(treats(guests))))
    print(str("Cost: $" + str(cost(tea_bags(guests), treats(guests)))))


def tea_bags(people: int) -> int:
    """returns the total number of tea bags given the number of guests"""
    return people * 2


def treats(people: int) -> int:
    """returns the total number of treats given the number of guests"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """returns the total cost given the number of treats and the number of tea bags)"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
