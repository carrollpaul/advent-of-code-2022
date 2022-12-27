with open("input.txt") as f:
    stream = f.read().rstrip()

    for i in range(0, len(stream) - 13):
        frame = stream[i : i + 14]

        if len(set(frame)) == 14:
            print(i + 14)
            break
