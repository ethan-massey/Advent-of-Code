class FloorGrid:

    def __init__(self):
        self.grid = []
        f = open('day04.txt', 'r')
        for line in f.readlines():
            self.grid.append(list(line.strip()))
        print(self.grid)

    def has_fewer_than_four_surrounding_paper_rolls(self, row, col) -> bool:
        surrounding_values = self.get_surrounding_values(row, col)
        return surrounding_values.count('@') < 4

    def get_accessible_rolls(self):
        count = []
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.get_value(r, c) == '@' and self.has_fewer_than_four_surrounding_paper_rolls(r, c):
                    count.append({
                        'row': r,
                        'col': c
                    })
        return count

    def remove_all_possible_rolls(self):
        num_removed_rolls = 0
        available_rolls = self.get_accessible_rolls()

        while len(available_rolls) > 0:
            for roll in available_rolls:
                self.grid[roll['row']][roll['col']] = '.'
                num_removed_rolls += 1
                print(f'removed a roll at {roll["row"]},{roll["col"]}')

            available_rolls = self.get_accessible_rolls()

        return num_removed_rolls

    def pick_up_roll(self, row, col):
        self.grid[row][col] = '.'

    def get_value(self, row, col):
        return self.grid[row][col]

    def is_valid_coord(self, row, col):
        return (row >= 0 and col >= 0) and (row < len(self.grid) and col < len(self.grid[0]))

    def get_surrounding_values(self, row, col):
        values = []
        row_indices = [row - 1, row, row + 1]
        col_indices = [col - 1, col, col + 1]

        for r in row_indices:
            for c in col_indices:
                if not (r == row and c == col) and self.is_valid_coord(r, c):
                    values.append(self.get_value(r, c))
        return values


floor_grid = FloorGrid()
print(len(floor_grid.get_accessible_rolls()))
print(floor_grid.remove_all_possible_rolls())
