stacks = [
    [],
    ['V','C','D','R','Z','G','B','W'],
    ['G','W','F','C','B','S','T','V'],
    ['C','B','S','N','W'],
    ['Q','G','M','N','J','V','C','P'],
    ['T','S','L','F','D','H','B'],
    ['J','V','T','W','M','N'],
    ['P','F','L','C','S','T','G'],
    ['B','D','Z'],
    ['M','N','Z','W']
]

with open('5/input.txt') as f:
    lines = f.readlines()
    lines = lines[10::]
    for line in lines:
        command = line.split()
        move = int(command[1])
        fromStack = int(command[3])
        to = int(command[5])
        while move > 0:
            stack = stacks[fromStack]
            removed = stack.pop()
            stacks[fromStack] = stack
            stacks[to] += removed
            move -= 1
    stackTops = ""
    for stack in stacks:
        if stack != []:
            stackTops += stack[-1]
    print(stackTops)


with open('5/input.txt') as f:
    lines = f.readlines()
    lines = lines[10::]
    for line in lines:
        command = line.split()
        move = int(command[1])
        fromStack = int(command[3])
        to = int(command[5])
        while move > 0:
            stack = stacks[fromStack]
            removed = stack[len(stack)-move::]
            stack = stack[0:len(stack)-move]
            stacks[fromStack] = stack
            stacks[to] += removed
            move -= move
    stackTops = ""
    for stack in stacks:
        if stack != []:
            stackTops += stack[-1]
    print(stackTops)
