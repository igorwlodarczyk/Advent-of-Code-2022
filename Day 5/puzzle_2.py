#     [C]         [Q]         [V]
#     [D]         [D] [S]     [M] [Z]
#     [G]     [P] [W] [M]     [C] [G]
#     [F]     [Z] [C] [D] [P] [S] [W]
# [P] [L]     [C] [V] [W] [W] [H] [L]
# [G] [B] [V] [R] [L] [N] [G] [P] [F]
# [R] [T] [S] [S] [S] [T] [D] [L] [P]
# [N] [J] [M] [L] [P] [C] [H] [Z] [R]

stacks = [
    ['N', 'R', 'G', 'P'],
    ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'],
    ['M', 'S', 'V'],
    ['L', 'S', 'R', 'C', 'Z', 'P'],
    ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'],
    ['C', 'T', 'N', 'W', 'D', 'M', 'S'],
    ['H', 'D', 'G', 'W', 'P'],
    ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'],
    ['R', 'P', 'F', 'L', 'W', 'G', 'Z']
]

with open('input1.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("move ", "")
        a, b = line.split(" from ")
        b, c = b.split(" to ")
        a = int(a)
        b = int(b)
        c = int(c)
        stacks[c - 1] = stacks[c - 1] + stacks[b - 1][-a:]
        stacks[b - 1] = stacks[b - 1][:-a]


for stack in stacks:
    print(stack[-1:], end='')

