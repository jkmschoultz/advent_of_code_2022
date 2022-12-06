with open("1/input.txt") as f:
    lines = f.readlines()
    i = 0
    elves = []
    for line in lines:
        if line == "\n":
            i += 1
        else:
            try:
                elves[i] += int(line)
            except Exception:
                elves.append(int(line))
    total = 0
    maximum = max(elves)
    print(maximum)
    elves.remove(maximum)
    total += maximum
    maximum = max(elves)
    elves.remove(maximum)
    total += maximum
    maximum = max(elves)
    elves.remove(maximum)
    total += maximum
    print(total)
