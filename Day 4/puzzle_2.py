with open('input1.txt') as f:
    sum = 0
    lines = f.readlines()
    for line in lines:
        sections = line.split(',')
        part1 = sections[0].split('-')
        part2 = sections[1].split('-')
        list1 = [_ for _ in range(int(part1[0]), int(part1[1]) + 1)]
        list2 = [_ for _ in range(int(part2[0]), int(part2[1]) + 1)]
        for number in list1:
            if number in list2:
                sum += 1
                break

print(sum)