with open('2/input.txt') as f:
    lines = f.readlines()
    points = 0
    for line in lines:
        turn = line.strip().split()
        if turn[0] == 'A' and turn[1] == 'X':
            points += 4
        elif turn[0] == "B" and turn[1] == "Y":
            points += 5
        elif turn[0] == "C" and turn[1] == "Z":
            points += 6
        elif turn[0] == "A" and turn[1] == "Y":
            points += 8
        elif turn[0] == "A" and turn[1] == "Z":
            points += 3
        elif turn[0] == "B" and turn[1] == "X":
            points += 1
        elif turn[0] == "B" and turn[1] == "Z":
            points += 9
        elif turn[0] == "C" and turn[1] == "X":
            points += 7
        elif turn[0] == "C" and turn[1] == "Y":
            points += 2
    print(points)


with open('2/input.txt') as f:
    lines = f.readlines()
    points = 0
    for line in lines:
        turn = line.strip().split()
        if turn[0] == 'A' and turn[1] == 'X':
            points += 3
        elif turn[0] == "B" and turn[1] == "X":
            points += 1
        elif turn[0] == "C" and turn[1] == "X":
            points += 2
        elif turn[0] == "A" and turn[1] == "Y":
            points += 4
        elif turn[0] == "B" and turn[1] == "Y":
            points += 5
        elif turn[0] == "C" and turn[1] == "Y":
            points += 6
        elif turn[0] == "A" and turn[1] == "Z":
            points += 8
        elif turn[0] == "B" and turn[1] == "Z":
            points += 9
        elif turn[0] == "C" and turn[1] == "Z":
            points += 7
    print(points)
