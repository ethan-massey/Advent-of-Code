
def partOne(days, lanternfish):
	new_list = []
	for i in range(0, days):
		for fish_ind in range(0, len(lanternfish)):
			if lanternfish[fish_ind] == 0:
				new_list.append(6)
				new_list.append(8)
			else:
				new_list.append(lanternfish[fish_ind] - 1)

		lanternfish = new_list
		new_list = []
		print('Day', i, 'computed')

	print('\nAnswer:', len(lanternfish), 'lanternfish')

def partTwo(days, lanternfish):
	d = {}
	for i in range(9):
		d[i] = 0

	for i in lanternfish:
		d[i] += 1

	# shift dict over each day
	for day in range(days):
		temp = d[0]

		d[0] = d[1]
		d[1] = d[2]
		d[2] = d[3]
		d[3] = d[4]
		d[4] = d[5]
		d[5] = d[6]
		d[6] = d[7]
		d[7] = d[8]
		# new guys
		d[8] = temp
		# 0 to 6
		d[6] += temp
		print('Day', day, 'computed')

	print('\nAnswer:', sum(d.values()), 'lanternfish')

def main():
	lines = open("data.txt", "r").readlines()
	lanternfish = lines[0].split(',')

	for i in range(0, len(lanternfish)):
		lanternfish[i] = int(lanternfish[i])

	prompt = 'Menu options:\n- 1:       PART 1 (O^2)\n- 2:       PART 2 (optimized)\n- <space>: EXIT\n\nEnter your choice: '

	choice = input(prompt)

	if(choice == '1'):
		days = int(input('Enter days of reproduction to simulate: '))
		partOne(days, lanternfish)
	elif(choice == '2'):
		days = int(input('Enter days of reproduction to simulate: '))
		partTwo(days, lanternfish)
	else:
		quit()


if __name__ == "__main__":
    main()
