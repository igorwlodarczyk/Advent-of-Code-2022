# Rock - 1
# Paper - 2
# Scissors - 3
# Rock A/X
# Paper B/Y
# Scissors C/Z
# 6 - win, 3 - draw, 0 - loss

with open('input1.txt') as f:
    points = 0
    lines = f.readlines()
    for line in lines:
        a = line.split()
        if a[1] == 'X':
            points += 1
            if a[0] == 'A':
                points += 3
            elif a[0] == 'C':
                points += 6
        elif a[1] == 'Y':
            points += 2
            if a[0] == 'B':
                points += 3
            elif a[0] == 'A':
                points += 6
        else:
            points += 3
            if a[0] == 'C':
                points += 3
            elif a[0] == 'B':
                points += 6
print(points)
