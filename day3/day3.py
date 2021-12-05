
def get_gamma_rate(one_bit_count: dict, num_count: int) -> str:
	gamma_rate = ''
	for i in one_bit_count.values():
		gamma_rate += ('0', '1')[i >= (num_count // 2)]
	return gamma_rate

# opp of gamma rate
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
	# format data
	bin_nums = open(datafile, "r").readlines()
	num_count = len(bin_nums)
	for i in range(0, num_count):
		bin_nums[i] = bin_nums[i].strip('\n')

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


def main():
    print(get_consumption_rate("data.txt"))
    

if __name__ == "__main__":
    main()
