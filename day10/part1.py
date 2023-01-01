cycle = 0
reg = 1
signals = []
crt = "\n"
pixel = 0


def check_interesting(cycle: int, reg: int, signals: list[int]) -> None:

    for val in [20, 60, 100, 140, 180, 220]:
        if cycle == val:
            signals.append(cycle * reg)


with open("input.txt") as f:
    for line in f.readlines():
        match line.split():
            case ["noop"]:
                inc = 1
                amt = 0
            case "addx", amt:
                inc = 2
                amt = int(amt)

        for _ in range(inc):
            cycle += 1

            # If the sprite position (register plus and minus 1) equals the cycle, draw a #, else draw a .
            # Every 40 cycles add a new line
            if cycle % 40 == 20:
                signals.append(cycle * reg)

            if pixel in [reg - 1, reg, reg + 1]:
                crt += "#"

            else:
                crt += "."

            pixel += 1
            if cycle % 40 == 0:
                crt += "\n"
                pixel = 0

        reg += amt

print(crt)
