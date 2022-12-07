with open('input1.txt') as f:
    sum = 0
    lines = f.readlines()
    for line in lines:
        sections = line.split(',')
        part1 = sections[0].split('-')
        part2 = sections[1].split('-')
        if int(part1[0]) <= int(part2[0]) and int(part1[1]) >= int(part2[1]):
            sum += 1
        elif int(part1[0]) >= int(part2[0]) and int(part1[1]) <= int(part2[1]):
            sum += 1
print(sum)