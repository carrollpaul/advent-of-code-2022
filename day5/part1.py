import re

from rich import print

columns = {
    "s1": ["H", "R", "B", "D", "Z", "F", "L", "S"],
    "s2": ["T", "B", "M", "Z", "R"],
    "s3": ["Z", "L", "C", "H", "N", "S"],
    "s4": ["S", "C", "F", "J"],
    "s5": ["P", "G", "H", "W", "R", "Z", "B"],
    "s6": ["V", "J", "Z", "G", "D", "N", "M", "T"],
    "s7": ["G", "L", "N", "W", "F", "S", "P", "Q"],
    "s8": ["M", "Z", "R"],
    "s9": ["M", "C", "L", "G", "V", "R", "T"],
}


with open("input.txt") as f:
    for line in f.readlines():
        amount, start, stop = map(int, re.findall("\d+", line))

        start = "s" + str(start)
        stop = "s" + str(stop)

        for _ in range(amount):
            try:
                columns[stop].append(columns[start].pop())
            except IndexError:
                continue

    ans = ""

    for col in columns.values():
        if col:
            ans += col[-1]

    print(ans)
