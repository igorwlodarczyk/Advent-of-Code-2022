def calculate_priority(char):
    a = ord(char)
    if a < 97:
        a -= 38
    else:
        a -= 96
    return a


with open('input1.txt') as f:
    sum_of_the_priorities = 0
    lines = f.readlines()
    for line in lines:
        line_length = len(line)
        part1 = line[0: int(line_length / 2)]
        part2 = line[int(line_length / 2): line_length]
        for item in part1:
            if item in part2:
                sum_of_the_priorities += calculate_priority(item)
                break

print(sum_of_the_priorities)