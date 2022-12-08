# adds a layer to the graph position.
def add_layer(pos_list):
	for pos in pos_list:
		cur_val = graph[pos[0]][pos[1]]
		if cur_val == '.':
			graph[pos[0]][pos[1]] = 1
		else:
			graph[pos[0]][pos[1]] = cur_val + 1

def parse_for_straight_comms(command_list) -> list:
	ret = []
	for comm in command_list:
		if comm[0][0] == comm[1][0]:
			ret.append(comm)
		elif comm[0][1] == comm[1][1]:
			ret.append(comm)
	return ret

# takes line end points and returns a list of coords to add a layer to
def get_straight_line(x1, y1, x2, y2) -> list:
	num_coords = max([abs(y2-y1)+1, abs(x2-x1)+1])
	x_vals = []
	y_vals = []
	ret = []

	if(y1 == y2):
		for val in range(min([x1, x2]), max(x1, x2)+1):
			x_vals.append(val)
		for i in range(0, num_coords):
			y_vals.append(y1)

	elif(x1 == x2):
		for val in range(min([y1, y2]), max(y1, y2)+1):
			y_vals.append(val)
		for i in range(0, num_coords):
			x_vals.append(x1)

	for i in range(0, num_coords):
		ret.append((x_vals[i], y_vals[i]))
	
	# example input: 0,1,0,5 -> [(0,1), (0,2), (0,3), (0,4), (0,5)]
	return ret

# takes line end points and returns a list of coords to add a layer to
def get_any_line(x1, y1, x2, y2) -> list:
	num_coords = max([abs(y2-y1)+1, abs(x2-x1)+1])
	x_vals = []
	y_vals = []
	ret = []

	for i in get_inclusive_range(x1, x2):
		x_vals.append(i)
	for i in get_inclusive_range(y1, y2):
		y_vals.append(i)

	# accout for any straight lines that _val list is len 1
	if(len(x_vals) == 1):
		for i in range(0, num_coords-1):
			x_vals.append(x_vals[0])
	elif(len(y_vals) == 1):
		for i in range(0, num_coords-1):
			y_vals.append(y_vals[0])

	# create tuple list
	for i in range(0, num_coords):
		ret.append((x_vals[i], y_vals[i]))

	# example input: 0,0,4,4 -> [(0,0), (1,1), (2,2), (3,3), (4,4)]
	return ret

# returns a list from n1 to n2 of values (inclusive)
# incrementing/decrementing by 1
def get_inclusive_range(n1, n2) -> list:
	ret = []
	if n1 > n2:
		for i in range(n1, n2-1, -1):
			ret.append(i)
	else:
		for i in range(n1, n2+1):
			ret.append(i)
	return ret

# return num of positions where at least 2 lines overlap
def get_num_coords_over_one():
	total = 0
	for r in range(0, rows):
		for c in range(0, cols):
			if graph[r][c] != '.':
				if graph[r][c] >= 2:
					total += 1

	return total


def printGraph(g):
	for r in g:
		print(r)
	print()

# return num of points at least 2 layers (only horiz or vert lines)
def getPartOneAnswer(command_list):
	command_list = parse_for_straight_comms(command_list)

	for comm in command_list:
		add_layer(get_straight_line(comm[0][0], comm[0][1], comm[1][0], comm[1][1]))

	return get_num_coords_over_one()

def getPartTwoAnswer(command_list):
	for comm in command_list:
		add_layer(get_any_line(comm[0][0], comm[0][1], comm[1][0], comm[1][1]))

	return get_num_coords_over_one()


#format data
lines = open("data.txt", "r").readlines()
max_x = 0
max_y = 0

command_list = []
for i in range(0, len(lines)):
	command_list.append(lines[i].strip().split(' -> '))

for i in range(0, len(command_list)):
	for n in range(0, len(command_list[i])):
		command_list[i][n] = command_list[i][n].split(',')
		command_list[i][n][0] = int(command_list[i][n][0])
		command_list[i][n][1] = int(command_list[i][n][1])
		max_x = (max_x, command_list[i][n][0])[command_list[i][n][0] > max_x]
		max_y = (max_y, command_list[i][n][1])[command_list[i][n][1] > max_y]

# command_list format:
# [command][command position][command position x or y]

# populate graph
rows, cols = (max_x+1, max_y+1)
graph = [['.' for i in range(cols)] for j in range(rows)]


prompt = 'Menu options:\n- 1:       PART 1\n- 2:       PART 2\n- <space>: EXIT\n\nEnter your choice: '

choice = input(prompt)

if(choice == '1'):
	print(getPartOneAnswer(command_list))
elif(choice == '2'):
	print(getPartTwoAnswer(command_list))
else:
	quit()
