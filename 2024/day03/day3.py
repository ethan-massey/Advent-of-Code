import re

# part 1
data = open("data.txt", "r").readlines()

mul_expressions = []
for line in data:
    mul_expressions += re.findall("mul\(\d{1,3},\d{1,3}\)", line.strip())


def mul(num1, num2):
    return int(num1) * int(num2)


sum = 0
for exp in mul_expressions:
    sum += eval(exp)

print(sum)

# part 2
process_pile = ""
should_we_keep_these_chars = True
for line in data:
    for i, c in enumerate(line):
        if i >= 6:
            if line[i - 7 : i] == "don't()":
                should_we_keep_these_chars = False
        if i >= 3:
            if line[i - 4 : i] == "do()":
                should_we_keep_these_chars = True
        if should_we_keep_these_chars:
            process_pile += c


mul_expressions = re.findall("mul\(\d{1,3},\d{1,3}\)", process_pile)

sum = 0
for exp in mul_expressions:
    sum += eval(exp)
print(sum)
