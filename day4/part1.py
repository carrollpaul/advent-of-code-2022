import re

count = 0

with open("input.txt") as f:
    for line in f.readlines():

        a, b, c, d = map(int, re.findall("\d+", line))

        if (a <= c and b >= d) or (c <= a and d >= b):
            count += 1


print(count)
