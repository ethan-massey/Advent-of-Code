# format data
lines = open("data.txt", "r").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

siblings = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}

def print_stack(stack):
    for i in stack:
        print(i, end=' ')
    print()

''' ---------------------- PART 1 ---------------------- '''
corrupt_points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

# return error points and stack for corrupt lines (returns 0 when line is not corrupt)
# (error points, stack)
def eval_line(line: str) -> tuple:
    char_stack = []
    for c in line:
        if c in siblings.values(): # opening tag
            char_stack.append(c)
        else:                    # closing tag
            top = char_stack.pop()
            if siblings[c] != top:
                char_stack.append(top)
                return (corrupt_points[c], char_stack)
    return (0, char_stack)

total = 0
for line in lines:
    total += eval_line(line)[0]
print(total)
''' ---------------------- PART 2 ---------------------- '''
inc_points = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

# return string of chars that completes the line
# input is stack from incomplete line
def complete_line(stack: list) -> str:
    ret = ''
    sib_copy = siblings
    sib_copy = {v: k for k, v in sib_copy.items()}
    for c in stack[::-1]:
        ret += sib_copy[c]
    return ret

# returns list of stacks that are not corrupt, AKA incomplete
def get_incomplete_stacks(lines: list) -> list:
    ret = []
    for line in lines:
        eval_output = eval_line(line)
        if eval_output[0] == 0:
            ret.append(eval_output[1])
    return ret

def get_completion_score(line: str) -> int:
    score = 0
    for c in line:
        score *= 5
        score += inc_points[c]
    return score


scores = []
incomplete = get_incomplete_stacks(lines)
for stack in incomplete:
    ending = complete_line(stack)
    score = get_completion_score(ending)
    scores.append(score)

# get middle score
scores.sort()
print(scores[len(scores) // 2])
