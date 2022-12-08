from collections import Counter

# PART 1 functions
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
	

# PART 2 functions
def get_gas_rating(datafile: str, gas_type: str) -> str:
	bin_nums = get_binary_nums(datafile)
	
	decreasing_list = bin_nums
	index = 0
	while(len(decreasing_list) > 1):
		decreasing_list = list_eval(decreasing_list, index, gas_type)
		index += 1
	O2_binary = decreasing_list[0]
	return bin_to_dec(O2_binary)


def list_eval(bin_list: list, i: int, gas_type: str) -> list:
	ret = []
	digit_count = {
		0 : 0,
		1 : 0
	}

	for num in bin_list:
		if num[i] == '1':
			digit_count[1] += 1
		else:
			digit_count[0] += 1

	if gas_type == 'O2':
		keep = ('1', '0')[digit_count[0] > digit_count[1]]
	elif gas_type == 'CO2':
		keep = ('0', '1')[digit_count[0] > digit_count[1]]

	for num in bin_list:
		if num[i] == keep:
			ret.append(num)

	return ret


def get_life_support(datafile: str) -> int:
	return get_gas_rating("data.txt", 'O2') * get_gas_rating("data.txt", 'CO2')


def main():
	prompt = 'Menu options:\n- 1:       PART 1\n- 2:       PART 2\n- <space>: EXIT\n\nEnter your choice: '
	choice = input(prompt)

	if(choice == '1'):
		print(get_consumption_rate("data.txt"))
	elif(choice == '2'):
		print(get_life_support("data.txt"))
	else:
		quit()


if __name__ == "__main__":
    main()
