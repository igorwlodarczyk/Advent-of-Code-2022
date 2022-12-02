# Rock - 1
# Paper - 2
# Scissors - 3
# Rock A
# Paper B
# Scissors C
# 6 - win, 3 - draw, 0 - loss
# X - loss, Y - draw, Z - win

with open('input1.txt') as f:
    points = 0
    lines = f.readlines()
    for line in lines:
        a = line.split()
        if a[1] == 'Z':
            points += 6
            if a[0] == 'A':
                points += 2
            elif a[0] == 'B':
                points += 3
            else:
                points += 1
        elif a[1] == 'Y':
            points += 3
            if a[0] == 'A':
                points += 1
            elif a[0] == 'B':
                points += 2
            else:
                points += 3
        else:
            if a[0] == 'A':
                points += 3
            elif a[0] == 'B':
                points += 1
            else:
                points += 2

print(points)

