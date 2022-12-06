with open('4/input.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        assigned = line.split(',')
        first = assigned[0].split('-')
        second = assigned[1].split('-')
        if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]) or \
            int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1]):
            total += 1
    print(total)

with open('4/input.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        assigned = line.split(',')
        first = assigned[0].split('-')
        second = assigned[1].split('-')
        totalr = range(int(first[0]), int((first[1]))+1)
        totalr2 = range(int(second[0]), int((second[1]))+1)
        if int(second[0]) in totalr or int(second[1]) in totalr:
            total += 1
        elif int(first[0]) in totalr2 or int(first[1]) in totalr2:
            total += 1
    print(total)