import string

priorities = dict(
    zip(list(string.ascii_lowercase) + list(string.ascii_uppercase), range(1, 53))
)

total = 0

with open("input.txt") as f:
    for line in f.readlines():
        middle = len(line) // 2
        left = set(line[:middle])
        right = set(line[middle:])

        common = list(left.intersection(right))

        total += priorities[common[0]]

print(total)
