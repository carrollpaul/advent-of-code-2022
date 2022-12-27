with open("input.txt") as f:
    stream = f.read().rstrip()

    for i in range(0, len(stream) - 3):
        frame = stream[i : i + 4]

        if len(set(frame)) == 4:
            print(i + 4)
            break
