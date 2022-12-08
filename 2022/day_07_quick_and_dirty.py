import copy
f = open('day_07.input', 'r')
history = [l.strip() for l in f.readlines()]

files = []
dir_sizes = {}

def read_history(history: list):
    line_num = 0
    cur_path = ''

    while line_num < len(history):
        line = history[line_num]
        
        # command
        if line[0] == '$':
            command = line.split()
            if command[1] == 'cd':
                if command[2] == '..':
                    # remove end of path
                    while cur_path[-1] != '/':
                        cur_path = cur_path[:-1]
                    if cur_path != '/':
                        cur_path = cur_path[:-1]
                else:
                    if not cur_path or cur_path[-1] == '/':
                        cur_path += command[2]
                    else:
                        cur_path += '/' + command[2]
        # dir contents
        else:
            size = line.split()[0]
            filename = line.split()[1]
            if size != 'dir':
                files.append({
                    'dir': copy.deepcopy(cur_path),
                    'name': filename,
                    'size': int(size)
                })

        line_num += 1



read_history(history)

def addSizeToParents(file):
    dir = file['dir']
    if dir != '/':
        while dir != '':
            while dir[-1] != '/':
                dir = dir[:-1]
            if dir != '/':
                dir = dir[:-1]
            if dir not in dir_sizes:
                dir_sizes[dir] = file['size']
            else:
                dir_sizes[dir] += file['size']
            if dir == '/':
                dir = ''


# get dir sizes
for f in files:
    if f['dir'] not in dir_sizes:
        dir_sizes[f['dir']] = f['size']
    else:
        dir_sizes[f['dir']] += f['size']
    addSizeToParents(f)


total = 0
for d in dir_sizes:
    if dir_sizes[d] <= 100000:
        total += dir_sizes[d]


print(total)

used_space = dir_sizes['/']
need_to_delete = 30000000-(70000000-used_space)
min_found = float('inf')
for d in dir_sizes:
    if dir_sizes[d] >= need_to_delete and dir_sizes[d] < min_found:
        min_found = dir_sizes[d]
print(min_found)
