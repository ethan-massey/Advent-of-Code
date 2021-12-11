# format data
lines = open("data.txt", "r").readlines()
digit_codings = []
output_vals = []
for i in range(len(lines)):
	single_digit_codings = lines[i].split(' | ')[0].strip().split(' ')
	single_output = lines[i].split(' | ')[1].strip().split(' ')
	digit_codings.append(single_digit_codings)
	output_vals.append(single_output)


def part_one():
	count_1478 = 0
	for output in output_vals:
		for i in range(4):
			if len(output[i]) == 2 or \
				len(output[i]) == 3 or \
				len(output[i]) == 4 or \
				len(output[i]) == 7:
					count_1478 += 1
	return count_1478

print(part_one())

def sort_strnum(n):
	return ''.join(sorted(n))

# returns a dict such that 
def get_number_aliases(encoded_nums: list) -> dict:
	num_aliases = {}
	char_aliases = {}

	# start with nums with unique lengths
	for num in encoded_nums:
		if len(num) == 2:
			num_aliases[1] = num
		elif len(num) == 4:
			num_aliases[4] = num
		elif len(num) == 3:
			num_aliases[7] = num
		elif len(num) == 7:
			num_aliases[8] = num

	# get 3
	to_get_e = []
	for num in encoded_nums:
		if len(num) == 5 and \
			num_aliases[1][0] in num and \
			num_aliases[1][1] in num:
				num_aliases[3] = num
	# get 'e'
	for num in encoded_nums:
		if len(num) == 5:
			to_get_e.append(num)
	to_get_e.append(num_aliases[4])
	
	char_aliases['e'] = diff(to_get_e)[0]
	# get 2
	for num in to_get_e:
		if diff(to_get_e)[0] in num:
			num_aliases[2] = num
	# get 5 and 9
	for num in encoded_nums:
		if len(num) == 5 and \
			num != num_aliases[2] and \
			num != num_aliases[3]:
				num_aliases[5] = num
		if len(num) == 6:
			if char_aliases['e'] not in num:
				num_aliases[9] = num
	# get 6 and 0
	for num in encoded_nums:
		if len(num) == 6 and \
			num != num_aliases[9]:
			if len(diff([num, num_aliases[1]])) == 4:
				num_aliases[0] = num
			else:
				num_aliases[6] = num

	return num_aliases

# feed output vals into alias dict and concat decoded string, return as int
def get_decoded_num(output_vals: list, encoded_nums: list) -> int:
	num_aliases = get_number_aliases(encoded_nums)
	num_aliases = {sort_strnum(v): str(k) for k, v in num_aliases.items()}
	ret = ''
	for num in output_vals:
		ret += num_aliases[sort_strnum(num)]
	return int(ret)

# takes list of strings, overlays the chars and returns list
# of chars not covered by another
# example: ['abc', 'bce', 'ab'] -> ['e']
def diff(str_list: list) -> list:
	ret = []
	times_seen = {
		'a' : 0,
		'b' : 0,
		'c' : 0,
		'd' : 0,
		'e' : 0,
		'f' : 0,
		'g' : 0
	}

	for s in str_list:
		s.split().sort()
		for c in set(s):
			times_seen[c] += 1

	for c in times_seen.keys():
		if times_seen[c] == 1:
			ret.append(c)

	return ret

def part_two():
	total = 0
	for i in range(len(digit_codings)):
		total += get_decoded_num(output_vals[i], digit_codings[i])
	return total

print(part_two())
