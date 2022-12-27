import string

from rich import print

priorities = dict(
    zip(list(string.ascii_lowercase) + list(string.ascii_uppercase), range(1, 53))
)

group = []
count = 0
total = 0
with open("input.txt") as f:
    lines = f.read().splitlines()

    for i in range(0, len(lines), 3):
        a, b, c = lines[i : i + 3]

        same = set(a) & set(b) & set(c)
        total += priorities[same.pop()]

print(total)
