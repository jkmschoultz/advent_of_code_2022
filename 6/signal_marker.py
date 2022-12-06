with open('6/input.txt') as f:
    text = f.readlines()[0]
    for i in range(len(text)):
        temp = text[i:i+4]
        unique = True
        for j in range(len(temp)):
            if temp[j] in temp[j+1::] :
                unique = False
                break
        if unique == True:
            print(i+4)
            break


with open('6/input.txt') as f:
    text = f.readlines()[0]
    for i in range(len(text)):
        temp = text[i:i+14]
        unique = True
        for j in range(len(temp)):
            if temp[j] in temp[j+1::] :
                unique = False
                break
        if unique == True:
            print(i+14)
            break