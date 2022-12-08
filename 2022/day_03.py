# =========================== PART 1 =============================== #
f = open('day_03.input', 'r')
rucksacks = [r.strip() for r in f.readlines()]
for i in range(len(rucksacks)):
	# split into compartment 1 and 2
	rucksacks[i] = {
		'comp1': rucksacks[i][:len(rucksacks[i])//2],
		'comp2': rucksacks[i][len(rucksacks[i])//2:]
	}

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = {l: p for p, l in enumerate(alphabet, start=1)}

# O(n) flex
def findDuplicate(list1, list2) -> str:
	d = {l: 1 for l in list1}
	for l in list2:
		if l in d:
			return l

# get priority sum
priority_total = 0
for r in rucksacks:
	common = findDuplicate(r['comp1'], r['comp2'])
	priority_total += priority[common]

print(priority_total)

# =========================== PART 2 =============================== #

# format (combine compartments)
rucksacks = [r['comp1'] + r['comp2'] for r in rucksacks]

def findDuplicate3lists(list1, list2, list3) -> str:
	d1 = {l: 1 for l in list1}
	d2 = {l: 1 for l in list2}
	for l in list3:
		if l in d1 and l in d2:
			return l

priority_total = 0
for i in range(0, len(rucksacks), 3):
	r1 = rucksacks[i]
	r2 = rucksacks[i+1]
	r3 = rucksacks[i+2]
	common = findDuplicate3lists(r1, r2, r3)
	priority_total += priority[common]

print(priority_total)
