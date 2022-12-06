characters = ['',"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ,"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

with open('3/input.txt') as f:
    sacks = f.readlines()
    total = 0
    for sack in sacks:
        first = sack[0:int(len(sack)/2)]
        second = sack[int(len(sack)/2)::]
        for letter in first:
            if letter in second:
                total += characters.index(letter)
                break
    print(total)

with open('3/input.txt') as f:
    sacks = f.readlines()
    total = 0
    i = 0
    moar = []
    while i + 3 <= len(sacks) :
        first = sacks[i]
        second = sacks[i+1]
        third = sacks[i+2]
        letters = []
        for letter in first:
            if letter in second and letter in third and letter not in letters:
                letters.append(letter)
                total += characters.index(letter)
                break
        i += 3
    print(total)
