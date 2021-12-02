
# format of [['forward', 2], ['down', 8]]
commands = open("commands.txt", "r").readlines()
for i in range(0, len(commands)):
	commands[i] = commands[i].strip('\n').split(' ')
	commands[i][1] = int(commands[i][1])

# Part 1
def get_end_position_times_two(commands) -> int:
	h_pos = 0
	depth = 0

	for com in commands:
		if com[0] == 'forward':
			h_pos += com[1]
		elif com[0] == 'down':
			depth += com[1]
		elif com[0] == 'up':
			depth -= com[1]

	return h_pos * depth

print(get_end_position_times_two(commands))


# Part 2