import copy
f = open('day_05.input', 'r')
lines = f.readlines()

stacks = {}
# create stacks structure and return line that begins procedure
def read_stacks():
    for line_num, line in enumerate(lines):
        stack_index = 1
        for i in range(1, len(line), 4):
            # done with stacks
            if line[i] == '1':
                return line_num + 2
            # no crate
            if line[i] != ' ':
                # if stack not created yet
                if stack_index not in stacks:
                    stacks[stack_index] = [line[i]]
                else:
                    stacks[stack_index].append(line[i])
            stack_index += 1

commands_linenum = read_stacks()
# sort by key
stacks = dict(sorted(stacks.items()))
# reverse crate order (parsed in reverse order)
for k in stacks:
    stacks[k] = stacks[k][::-1]

# ======================== PART 1 ===================================== #
stack1 = copy.deepcopy(stacks)

def move_operation(stack_struct, from_stack, to_stack, num_crates):
    for i in range(num_crates):
        crate = stack_struct[from_stack].pop()
        stack_struct[to_stack].append(crate)

# parse commands
for comm in lines[commands_linenum:]:
    comm = comm.split()
    num_crates = int(comm[1])
    from_stack = int(comm[3])
    to_stack = int(comm[5])
    move_operation(stack1, from_stack, to_stack, num_crates)

def get_top_items(stack_struct):
    ret = ''
    for k in stack_struct:
        ret += stack_struct[k][-1]
    print(ret)

get_top_items(stack1)

# ======================== PART 2 ===================================== #
stack2 = copy.deepcopy(stacks)

def move_operation_9001(stack_struct, from_stack, to_stack, num_crates):
    # get crates
    crates = stack_struct[from_stack][-num_crates:]
    # remove crates from from_stack
    stack_struct[from_stack] = stack_struct[from_stack][:-num_crates]
    # add crates to to_stack
    stack_struct[to_stack] += crates

# parse commands
for comm in lines[commands_linenum:]:
    comm = comm.split()
    num_crates = int(comm[1])
    from_stack = int(comm[3])
    to_stack = int(comm[5])
    move_operation_9001(stack2, from_stack, to_stack, num_crates)

get_top_items(stack2)
