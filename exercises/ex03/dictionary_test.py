__author__ = "730765813"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert1() -> None:
    """Tests if invert works for an empty dict"""
    assert invert({}) == {}


def test_invert2() -> None:
    """Tests if inverts correctly"""
    assert invert({"1": "one", "2": "two", "3": "three"}) == {
        "one": "1",
        "two": "2",
        "three": "3",
    }


def test_invert3() -> None:
    """Tests if inverts correctly with longer dict"""
    assert invert({"borger": "fries", "cup": "coke", "ew": "salad"}) == {
        "fries": "borger",
        "coke": "cup",
        "salad": "ew",
    }


def test_count1() -> None:
    """Tests if count works with an empty list"""
    assert count([]) == {}


def test_count2() -> None:
    """Tests if count correctly counts each item"""
    assert count(["burger", "burger", "burger", "nuggy", "nuggy", "salad"]) == {
        "burger": 3,
        "nuggy": 2,
        "salad": 1,
    }


def test_count3() -> None:
    """Tests if count correctly counts each item"""
    assert count(
        ["1", "2", "2", "1", "3", "234212414", "2", "1", "3", "234212414"]
    ) == {"1": 3, "2": 3, "3": 2, "234212414": 2}


def test_favorite_color1() -> None:
    """Tests if orange wins the tie"""
    assert (
        favorite_color(
            {
                "timmy": "orange",
                "robert": "orange",
                "matthew": "red",
                "jack": "blue",
                "max": "blue",
            }
        )
        == "orange"
    )


def test_favorite_color2() -> None:
    """Tests if function returns black"""
    assert (
        favorite_color(
            {
                "timmy": "black",
                "robert": "black",
                "matthew": "red",
                "jack": "blue",
            }
        )
        == "black"
    )


def test_favorite_color3() -> None:
    """Tests if function returns "yeller" for a longer dict"""
    assert (
        favorite_color(
            {
                "borger": "yeller",
                "frites": "yeller",
                "tom clancy": "rainbow",
                "hadi": "yeller",
                "jack": "blue",
                "sky": "blue",
            }
        )
        == "yeller"
    )


def test_bin_len1() -> None:
    """Tests if the set for length 5 only includes one mommy"""
    assert bin_len(["mommy", "mommy", "mommy", "googa", "gagoo", "ben"]) == {
        5: {"gagoo", "googa", "mommy"},
        3: {"ben"},
    }


def test_bin_len2() -> None:
    """Tests if function correctly sorts strings by length"""
    assert bin_len(["borger", "froiz", "squid", "ben", "tod"]) == {
        6: {"borger"},
        5: {"froiz", "squid"},
        3: {"tod", "ben"},
    }


def test_bin_len3() -> None:
    """Tests if function correctly sorts strings by length"""
    assert bin_len(["1", "23", "23423", "5"]) == {
        1: {"1", "5"},
        2: {"23"},
        5: {"23423"},
    }
