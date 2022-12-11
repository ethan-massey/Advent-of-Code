f = open('day_10.input', 'r')
lines = f.readlines()

# ======================== PART 1 ========================== #

register_x = {1: 1}
cur_cycle = 1

for line in lines:

    if line.strip() == 'noop':
        register_x[cur_cycle+1] = register_x[cur_cycle]
        cur_cycle += 1

    else:
        add_value = int(line.strip().split()[1])
        register_x[cur_cycle + 1] = register_x[cur_cycle]
        register_x[cur_cycle + 2] = register_x[cur_cycle] + add_value
        cur_cycle += 2

strength_sum = 0
for cycle in range(20, len(register_x), 40):
    strength_sum += register_x[cycle] * cycle

print(strength_sum)

# delete any cycles over 240, not needed for CRT
cur_cycle = 241
while cur_cycle in register_x:
    del register_x[cur_cycle]
    cur_cycle += 1

# ======================== PART 2 ========================== #

image = ''

for cycle in register_x:

    sprite_pixels = [register_x[cycle] - 1, register_x[cycle], register_x[cycle] + 1]
    if (cycle - 1) % 40 in sprite_pixels:
        image += '#'
    else:
        image += '.'

    if cycle % 40 == 0:
        image += '\n'

print(image)
