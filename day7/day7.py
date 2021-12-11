import statistics

def part_one(h_positions):
	med = statistics.median(h_positions)

	distances = {}
	# populate dict. key = index, val = distance to median
	for i in range(len(h_positions)):
		distances[i] = abs(med-h_positions[i])

	return int(sum(distances.values()))

# Using triangle sum for Part 2
def get_fuel_amount(start, end):
	n = abs(end - start)
	total = 0
	for i in range(n, 0, -1):
		total += i
	return total 

def part_two(h_positions):
	fuel_amounts = []
	max_pos = max(h_positions)

	for i in range(max_pos+1):
		fuel_sum = 0
		for h_pos_ind in range(len(h_positions)):
			fuel_sum += get_fuel_amount(h_positions[h_pos_ind], i)
		print('Done computing', str(round((i / float(max_pos+1) * 100), 1)) + '%')
		fuel_amounts.append(fuel_sum)

	return min(fuel_amounts)

def main():
	# format data
	h_positions = open("data.txt", "r").readlines()[0].split(',')
	for i in range(len(h_positions)):
		h_positions[i] = int(h_positions[i])
	h_positions.sort()

	prompt = 'Menu options:\n- 1:       PART 1\n- 2:       PART 2\n- <space>: EXIT\n\nEnter your choice: '

	choice = input(prompt)

	if(choice == '1'):
		print(part_one(h_positions))
	elif(choice == '2'):
		print(part_two(h_positions))
	else:
		quit()


if __name__ == "__main__":
    main()

