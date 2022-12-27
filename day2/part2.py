letter_converter = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

win_lose = {
    "rock": {"lose": "scissors", "win": "paper", "draw": "rock"},
    "paper": {"lose": "rock", "win": "scissors", "draw": "paper"},
    "scissors": {"lose": "paper", "win": "rock", "draw": "scissors"},
}

scores = {"win": 6, "draw": 3, "lose": 0}

values = {"rock": 1, "paper": 2, "scissors": 3}


def score(
    pair: list[str],
    letter_converter: dict[str, str],
    win_lose: dict[str, dict[str, int]],
    values: dict[str, int],
) -> int:
    left = letter_converter.get(pair[0])
    right = letter_converter.get(pair[1])

    score = scores[right]  # type: ignore

    symbol = win_lose[left][right]

    symbol_value = values[symbol]

    return score + symbol_value


total = 0
with open("input.txt") as f:
    for line in f.readlines():
        pair = line.split()

        total += score(pair, letter_converter, win_lose, values)

    print(total)
