f = open('day_08.input', 'r')
lines = [line.strip() for line in f.readlines()]

tree_heights = []
for line in lines:
    grid_row = []
    for char in line:
        grid_row.append(int(char))
    tree_heights.append(grid_row)


def print_grid(grid):
    for r in grid:
        row = ''
        for c in r:
            row += str(c) + '\t'
        print(row)


# print_grid(tree_heights)


def check_visible_left(grid: list, r: int, c: int) -> bool:
    row = grid[r]
    for i in range(c):
        if row[i] >= grid[r][c]:
            return False
    return True


def check_visible_right(grid: list, r: int, c: int) -> bool:
    row = grid[r]
    for i in range(c+1, len(row)):
        if row[i] >= grid[r][c]:
            return False
    return True


def check_visible_up(grid: list, r: int, c: int) -> bool:
    for i in range(r):
        if grid[i][c] >= grid[r][c]:
            return False
    return True


def check_visible_down(grid: list, r: int, c: int) -> bool:
    for i in range(r+1, len(grid)):
        if grid[i][c] >= grid[r][c]:
            return False
    return True
    

def get_number_visible(tree_grid: list) -> int:
    num_visible = (len(tree_grid) * 2) + ((len(tree_grid[0]) - 2) * 2)

    for r in range(1, len(tree_grid)-1):
        for c in range(1, len(tree_grid[0])-1):
            if check_visible_left(tree_grid, r, c) or \
                    check_visible_right(tree_grid, r, c) or \
                    check_visible_up(tree_grid, r, c) or \
                    check_visible_down(tree_grid, r, c):
                num_visible += 1
    
    return num_visible


def get_left_score(grid: list, r: int, c: int) -> int:
    score = 0

    row = grid[r]
    for i in range(c-1, -1, -1):
        score += 1
        if row[i] >= grid[r][c]:
            return score

    return score


def get_right_score(grid: list, r: int, c: int) -> int:
    score = 0

    row = grid[r]
    for i in range(c+1, len(row)):
        score += 1
        if row[i] >= grid[r][c]:
            return score

    return score


def get_up_score(grid: list, r: int, c: int) -> int:
    score = 0

    for row in range(r-1, -1, -1):
        score += 1
        if grid[row][c] >= grid[r][c]:
            return score

    return score


def get_down_score(grid: list, r: int, c: int) -> int:
    score = 0

    for row in range(r+1, len(grid)):
        score += 1
        if grid[row][c] >= grid[r][c]:
            return score

    return score


def get_highest_scenic_score(tree_grid: list) -> int:
    best_score = 0

    for r in range(1, len(tree_grid)-1):
        for c in range(1, len(tree_grid[0])-1):
            up_score = get_up_score(tree_grid, r, c)
            down_score = get_down_score(tree_grid, r, c)
            left_score = get_left_score(tree_grid, r, c)
            right_score = get_right_score(tree_grid, r, c)

            total = up_score * down_score * left_score * right_score

            best_score = max(total, best_score)

    return best_score


print(get_number_visible(tree_heights))

print(get_highest_scenic_score(tree_heights))
