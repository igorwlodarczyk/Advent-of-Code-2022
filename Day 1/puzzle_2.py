with open('input1.txt') as f:
    lines = f.readlines()
    a = 0
    elves_list = []
    for line in lines:
        if line != '\n':
            a += int(line)
        else:
            elves_list.append(a)
            a = 0
    elves_list.sort(reverse=True)
    result = elves_list[0] + elves_list[1] + elves_list[2]
    print(result)

