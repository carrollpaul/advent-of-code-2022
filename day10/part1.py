cycle = 0
reg = 1
signals = []
crt = "\n"
pixel = 0

with open("input.txt") as f:
    for line in f.readlines():
        match line.split():
            case ["noop"]:
                inc = 1  # Number of cycles to process
                amt = 0  # Amount to add to register after cycles processed
            case "addx", amt:
                inc = 2
                amt = int(amt)

        for _ in range(inc):
            cycle += 1  # Start of cycle

            if cycle % 40 == 20:
                signals.append(cycle * reg)

            # If one of the three sprite positions (register plus and minus 1) is at target pixel, draw a #, else draw a .
            if pixel in [reg - 1, reg, reg + 1]:
                crt += "#"
            else:
                crt += "."

            pixel += 1  # End of cycle

            # Every 40 cycles add a new line and reset the pixel to 0
            if cycle % 40 == 0:
                crt += "\n"
                pixel = 0

        reg += amt

print(crt)  # EJCFPGLH
print(sum(signals))  # 11960
