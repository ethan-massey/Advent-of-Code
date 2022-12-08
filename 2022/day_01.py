f = open('day_01.input', 'r')
lines = f.readlines()

# find max calorie elf (PART 1)
max_elf = float('-inf')
cur_elf = float('-inf')
for i in range(len(lines)):
    if lines[i] == '\n':
        max_elf = max(max_elf, cur_elf)
        cur_elf = 0
    else:
        cur_elf += int(lines[i])

print(max_elf)

# find sum of top 3 (PART 2)
top3 = [float('-inf'), float('-inf'), float('-inf')]
cur_elf = float('-inf')

for i in range(len(lines)):
    if lines[i] == '\n':
        # if elf is > top 1, make him top one and shift others down, etc
        if cur_elf > top3[2]:
            top3[0] = top3[1]
            top3[1] = top3[2]
            top3[2] = cur_elf
        elif cur_elf > top3[1]:
            top3[0] = top3[1]
            top3[1] = cur_elf
        elif cur_elf > top3[0]:
            top3[0] = cur_elf
        cur_elf = 0
    else:
        cur_elf += int(lines[i])

print(sum(top3))
