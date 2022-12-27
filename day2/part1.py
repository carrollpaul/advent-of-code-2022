# a rock
# b paper
# c scissors

# x rock
# y paper
# z scissors

# 1 rock
# 2 paper
# 3 scissors

# 0 lose
# 3 draw
# 6 win


score = 0


letter_converter = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

win_lose = {
    "rock": {"paper": 6, "scissors": 0},
    "paper": {"scissors": 6, "rock": 0},
    "scissors": {"rock": 6, "paper": 0},
}

values = {"rock": 1, "paper": 2, "scissors": 3}


def score(
    pair: list[str],
    letter_converter: dict[str, str],
    win_lose: dict[str, dict[str, int]],
    values: dict[str, int],
) -> int:
    left = letter_converter.get(pair[0])
    right = letter_converter.get(pair[1])

    val = values[right]  # type: ignore
    if left == right:
        return 3 + val

    return win_lose[left][right] + val  # type: ignore


total = 0
with open("input.txt") as f:
    for line in f.readlines():
        pair = line.split()

        total += score(pair, letter_converter, win_lose, values)

    print(total)
