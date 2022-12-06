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
    i = 0
    while i < len(lines):
        bag1 = lines[i]
        bag2 = lines[i + 1]
        bag3 = lines[i + 2]
        i += 3
        for item in bag1:
            if item in bag2 and item in bag3:
                sum_of_the_priorities += calculate_priority(item)
                break
print(sum_of_the_priorities)