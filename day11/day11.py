# format data
def format_data(datafile: str) -> list:
    octopi = []
    lines = open(datafile, "r").readlines()
    for line in lines:
        octopi.append([int(i) for i in list(line.strip())])
    return octopi


def get_valid_neighbors(octopi: list, r: int, c: int) -> list:
    neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1), (r+1, c+1), (r-1, c-1), (r+1, c-1), (r-1, c+1)]
    valid = []
    for r, c in neighbors:
        if 0 <= r < len(octopi) and 0 <= c < len(octopi[0]):
            valid.append((r, c))
    return valid


def flash(octopi: list, r: int, c: int):
    neighbors = get_valid_neighbors(octopi, r, c)
    for row, col in neighbors:
        octopi[row][col] += 1


# return num flashers after completing one step
def process_step(octopi: list) -> int:
    all_flashers = []
    current_flashers = []
    for r in range(len(octopi)):
        for c in range(len(octopi[0])):
            # add one to all octopi
            octopi[r][c] += 1
            # get first flashers
            if octopi[r][c] > 9:
                all_flashers.append((r, c))
                current_flashers.append((r, c))

    while len(current_flashers) > 0:
        # flash the octopi found
        for row, col in current_flashers:
            flash(octopi, row, col)
        current_flashers = []

        # check for new octopi to flash
        for r in range(len(octopi)):
            for c in range(len(octopi[0])):
                if octopi[r][c] > 9 and (r, c) not in all_flashers:
                    all_flashers.append((r, c))
                    current_flashers.append((r, c))

    # set those that flashed to 0
    for r, c in all_flashers:
        octopi[r][c] = 0

    return len(all_flashers)


def get_day_of_megaflash(octopi: list) -> int:
    num_flashes = 0
    day = 0
    while num_flashes != len(octopi) * len(octopi[0]):
        num_flashes = process_step(octopi)
        day += 1
    return day


def main():
    octopi = format_data("data.txt")
    num_flashes = 0
    for step in range(100):
        num_flashes += process_step(octopi)
    print('Part 1:', num_flashes)
    print('Part 2:', get_day_of_megaflash(octopi), 'days')


if __name__ == "__main__":
    main()