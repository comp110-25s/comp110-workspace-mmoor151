"Guess a 5 letter word"

__author__ = "730765813"


def contains_char(goal: str, letter: str) -> bool:
    """Tells if there is a correct letter but in the wrong location"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    idx: int = 0
    while idx < len(goal):
        if goal[idx] == letter:
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Tells if the letters match in any way through emojis"""
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"
    result = ""
    idx = 0
    assert len(guess) == len(secret), "Guess must be same length as secret"
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1
    return result


def input_guess(expected_length: int) -> str:
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    print(f"=== Turn {turn}/6 ===")
    guess = input_guess(len(secret))
    print(emojified(guess, secret))
    while secret != guess and turn < 6:
        turn = turn + 1
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
    if turn < 6:
        print(f"You won in {turn}/6 turns!")
    if turn >= 6:
        print(f"x/6 - Sorry, try again tomorrow!")
