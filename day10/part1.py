cycle = 0
reg = 1
signals = []


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
            check_interesting(cycle, reg, signals)

        reg += amt

print(sum(signals))
