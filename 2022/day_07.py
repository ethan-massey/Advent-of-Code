import copy
f = open('day_07.input', 'r')
history = [l.strip() for l in f.readlines()]


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __lt__(self, other):
        return self.name < other.name


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []        # list of Files
        self.directories = []  # list of Directories
        # if not root
        if self.parent:
            # if parent is root
            if self.parent.absolute_path == '/':
                # just add name
                self.absolute_path = parent.absolute_path + name
                # otherwise add / + name
            else:
                self.absolute_path = parent.absolute_path + '/' + name
        else:
            self.absolute_path = '/'
        self.size = 0

    def __lt__(self, other):
        return self.name < other.name

    # add file to current dir and add file size to current dir and all parents
    def add_file(self, file: File):
        self.files.append(file)

        def add_size_to_parent_dir(dir: Directory, file_size: int):
            dir.size += file_size
            if not dir.parent:
                return
            add_size_to_parent_dir(dir.parent, file_size)

        add_size_to_parent_dir(self, file.size)

    def add_dir(self, dir):
        self.directories.append(dir)


root = Directory('/', None)


def read_terminal_history(history: list) -> Directory:
    cur_dir = root
    cur_line_num = 1

    while cur_line_num < len(history):
        line = history[cur_line_num].split()

        # command
        if line[0] == '$':
            if line[1] == 'cd':
                # new dir
                if line[2] != '..':
                    new_dir = Directory(line[2], cur_dir)
                    cur_dir.add_dir(new_dir)
                    cur_dir = new_dir
                # go back a dir
                else:
                    cur_dir = cur_dir.parent

        # dirs and files
        else:
            # file
            if line[0] != 'dir':
                new_file = File(line[1], int(line[0]))
                cur_dir.add_file(new_file)

        cur_line_num += 1


def find_sum_all_dirs_size_at_most_n(root: Directory, max_size: int):
    ret = []

    def get_dirs(cur_dir):
        if cur_dir.size <= max_size:
            ret.append(cur_dir.size)
        for d in cur_dir.directories:
            get_dirs(d)

    get_dirs(root)
    return sum(ret)


read_terminal_history(history)

print(find_sum_all_dirs_size_at_most_n(root, 100000))


def find_smallest_dir_to_free_space(root: Directory):
    space_needed = 30000000 - (70000000 - root.size)

    def get_size(cur_dir):
        global SMALLEST_SIZE
        if space_needed <= cur_dir.size < SMALLEST_SIZE:
            SMALLEST_SIZE = cur_dir.size
        for d in cur_dir.directories:
            get_size(d)

    get_size(root)
    return SMALLEST_SIZE


SMALLEST_SIZE = float('inf')
print(find_smallest_dir_to_free_space(root))


def print_directory(dir: Directory):
    ret = {'value': ['\033[93m' + '/']}

    def add_lines(root: Directory, indent: str):
        contents = root.files + root.directories
        contents.sort()

        for thing in contents:
            if thing.__class__.__name__ == 'File':
                ret['value'].append('\033[95m' + indent + thing.name + ' ' + str(thing.size))
            elif thing.__class__.__name__ == 'Directory':
                ret['value'].append('\033[93m' + indent + thing.absolute_path)
                add_lines(thing, indent + '\t')

    add_lines(dir, '\t')
    for line in ret['value']:
        print(line)

print_directory(root)