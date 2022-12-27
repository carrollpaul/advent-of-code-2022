import re

count = 0

with open("input.txt") as f:
    for line in f.readlines():

        a, b, c, d = map(int, re.findall("\d+", line))

        s1 = {i for i in range(a, b + 1)}
        s2 = {i for i in range(c, d + 1)}

        if s1.intersection(s2):
            count += 1

print(count)
