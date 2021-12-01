
def get_increasing_depths(datafile):

	depths = open(datafile, "r").readlines()

	# total of measurements > than previous measurement
	total = 0

	for i in range(1, len(depths)):
		format_depth = int(depths[i].strip('\n'))
		prev_format_depth = int(depths[i-1].strip('\n'))
		# if measurement > previous measurement
		if format_depth > prev_format_depth:
			total += 1

	return total


print(get_increasing_depths("depths.txt"))