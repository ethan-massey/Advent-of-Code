class BankCase:

    def __init__(self):
        f = open('day03.txt', 'r')
        str_banks = [list(l.strip()) for l in f.readlines()]
        self.banks = [[int(n) for n in bank] for bank in str_banks]


    def get_highest_joltage(self, bank: list) -> int:
        total = ''
        bank_copy = bank[:]

        max_val = max(bank_copy[:-1])
        total += str(max_val)
        max_ind = bank_copy.index(max_val)
        del bank_copy[max_ind]

        max_val = max(bank_copy[max_ind:])
        total += str(max_val)
        del bank_copy[bank_copy.index(max_val)]

        return int(total)


    def get_highest_joltage_v2(self, bank: list) -> int:
        total = ''
        bank_copy = bank[:]

        for i in range(12, 0, -1):
            available_nums = bank_copy[:len(bank_copy)-i+1]
            max_val = max(available_nums)
            total += str(max_val)
            max_ind = bank_copy.index(max_val)
            bank_copy = bank_copy[max_ind+1:]

        return int(total)


    def get_total_highest_joltage(self, version) -> int:
        total = 0
        if version == 'v1':
            for b in self.banks:
                total += self.get_highest_joltage(b)
        elif version == 'v2':
            for b in self.banks:
                total += self.get_highest_joltage_v2(b)
        return total


bank_case = BankCase()
print(bank_case.get_total_highest_joltage('v1'))
print(bank_case.get_total_highest_joltage('v2'))
