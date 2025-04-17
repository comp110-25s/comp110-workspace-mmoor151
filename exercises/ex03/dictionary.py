__author__ = "730765813"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    dict_output = {}
    for key in dict_input:
        if dict_input[key] in dict_output:
            raise KeyError("You have duplicate keys")
        dict_output[dict_input[key]] = key
    return dict_output


def count(list_input: list[str]) -> dict[str, int]:
    dict_output = {}
    for item in list_input:
        if item in dict_output:
            dict_output[item] += 1
        else:
            dict_output[item] = 1
    return dict_output


def favorite_color(dict_input: dict[str, str]) -> str:
    favorite_colors = []
    for key in dict_input:
        favorite_colors.append(dict_input[key])
    counted_colors = count(favorite_colors)
    max_color = ""
    max_number = 0
    for color in counted_colors:
        if counted_colors[color] > max_number:
            max_color = color
            max_number = counted_colors[color]
    return max_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    bin = {}
    for thingy in strings:
        if len(thingy) in bin:
            bin[len(thingy)].add(thingy)
        else:
            bin[len(thingy)] = {thingy}
    return bin
