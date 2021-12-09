
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

rows, cols = (max_x, max_y)
graph = [['.' for i in range(cols)] for j in range(rows)]

# adds a layer to the graph position.
def add_layer(x_pos, y_pos):
	cur_val = graph[x_pos][y_pos]
	if cur_val == '.':
		graph[x_pos][y_pos] = 1
	else:
		graph[x_pos][y_pos] = cur_val + 1

# takes line end points and returns a list of coords to add a layer to
def get_straight_line(x1, y1, x2, y2):
	ret = []
	
	# example input: 0,1,0,5 -> [(0,1), (0,2), (0,3), (0,4), (0,5)]
	return ret


# return num of positions where at least 2 lines overlap
def get_num_coords_over_one():
	total = 0
	for r in range(0, max_x):
		for c in range(0, max_y):
			if graph[r][c] != '.':
				if graph[r][c] >= 2:
					total += 1

	return total











