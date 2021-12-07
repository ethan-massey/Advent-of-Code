from collections import Counter

def get_gamma_rate(one_bit_count: dict, num_count: int) -> str:
	gamma_rate = ''
	for i in one_bit_count.values():
		gamma_rate += ('0', '1')[i >= (num_count // 2)]
	return gamma_rate


def get_epsilon_rate(gamma_rate: str) -> str:
	ep_rate = ''
	for i in range(0, len(gamma_rate)):
		ep_rate += ('0', '1')[gamma_rate[i] == '0']
	return ep_rate


def bin_to_dec(bin_num: str) -> int:
	dec = 0
	bin_reverse = bin_num[::-1]
	factor = 1
	for i in range(0, len(bin_num)):
		dec += int(bin_reverse[i]) * factor
		factor *= 2
	return dec


def get_consumption_rate(datafile: str) -> int:
	bin_nums = get_binary_nums(datafile)
	num_count = len(bin_nums)

	# num of 1 bits at each index
	one_bit_count = {}
	for i in range(0, len(bin_nums[0])):
		one_bit_count[i] = 0

	# populate dict
	for i in range(0, num_count):
		for ind in range(0, len(bin_nums[i])):
			if bin_nums[i][ind] == '1':
				one_bit_count[ind] += 1


	gamma = get_gamma_rate(one_bit_count, num_count)
	epsilon = get_epsilon_rate(gamma)
	gamma = bin_to_dec(gamma)
	epsilon = bin_to_dec(epsilon)
	return gamma * epsilon

def get_binary_nums(datafile: str) -> list:
	# format data
	bin_nums = open(datafile, "r").readlines()
	num_count = len(bin_nums)
	for i in range(0, num_count):
		bin_nums[i] = bin_nums[i].strip('\n')
	return bin_nums

def get_O2_rating(datafile: str) -> int:
	bin_nums = get_binary_nums(datafile)

	# ind = 0
	# while len(bin_nums) > 1:
	# 	bin_nums.sort(key = lambda x: x[ind])

	# 	if bin_nums[(len(bin_nums)//2)] == '1':
	# 		bin_nums = [ elem for elem in bin_nums if elem[ind] == '1']
	# 	else:
	# 		bin_nums = [ elem for elem in bin_nums if elem[ind] == '0']

	# 	print(bin_nums[(len(bin_nums)//2)], ind)
	# 	ind += 1
	# 	# bottom
	# return bin_nums[0]

	ind = 0
	while len(bin_nums) > 1:
		ind_nums = [ elem[ind] for elem in bin_nums ]
		most_common = Counter(ind_nums).most_common()[0][0]

		first_one_index = ind_nums.index('1')

		bin_nums = (bin_nums[first_one_index:], bin_nums[:first_one_index])[most_common == '0']

		for i, val in enumerate(bin_nums):
			print(i, val)

		ind += 1

	return bin_nums[0]







def get_life_support_rate(datafile: str) -> int:
	O2_rating = get_O2_rating(datafile)
	CO2_scrubber_rating = get_CO2_scrubber_rating()
	return O2_rating * CO2_scrubber_rating



def main():
    # print(get_consumption_rate("data.txt"))
    # print(get_life_support_rate("data.txt"))
    print(get_O2_rating("data.txt"))


if __name__ == "__main__":
    main()
