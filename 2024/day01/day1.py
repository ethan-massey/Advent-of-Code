data = open("data.txt", "r")
lines = data.readlines()

left_list = []
right_list = []

# format data
for line in lines:
    line = line.strip()
    left_list.append(int(line.split(" ")[0]))
    right_list.append(int(line.split(" ")[-1]))

LEFT_LIST_SORTED = sorted(left_list)
RIGHT_LIST_SORTED = sorted(right_list)

sum = 0

for i in range(len(LEFT_LIST_SORTED)):
    sum += abs(LEFT_LIST_SORTED[i] - RIGHT_LIST_SORTED[i])

print("part 1:", sum)

# part 2

# get frequencies
frequencies = {k: 0 for k in LEFT_LIST_SORTED}
for k in frequencies:
    frequencies[k] = RIGHT_LIST_SORTED.count(k)

# get similarity score
sim_score = 0
for num in LEFT_LIST_SORTED:
    sim_score += num * frequencies[num]

print(sim_score)
