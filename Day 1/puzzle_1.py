with open('input1.txt') as f:
    lines = f.readlines()
    a = 0
    b = 0
    for line in lines:
        if line != '\n':
            b += int(line)
        else:
            if b > a:
                a = b
                b = 0
            else:
                b = 0
    print(a)
