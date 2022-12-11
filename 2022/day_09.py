import copy
f = open('day_09.input')
commands = f.readlines()
for i in range(len(commands)):
    commands[i] = {
        'dir': commands[i].split()[0],
        'steps': int(commands[i].split()[1])
    }
'''
commands = [
{'dir': 'R', 'steps': 4}
{'dir': 'U', 'steps': 4}
{'dir': 'L', 'steps': 3}
{'dir': 'D', 'steps': 1}
{'dir': 'R', 'steps': 4}
{'dir': 'D', 'steps': 1}
{'dir': 'L', 'steps': 5}
{'dir': 'R', 'steps': 2}
]
'''


def close_enough(head, tail):
    if abs(head['x'] - tail['x']) <= 1 and abs(head['y'] - tail['y']) <= 1:
        return True
    return False


# takes dict coord and direction and return moved coord
def move_coord(coord, direction) -> dict:
    new_coord = copy.deepcopy(coord)
    if direction == 'U':
        new_coord['y'] += 1

    elif direction == 'D':
        new_coord['y'] -= 1

    elif direction == 'L':
        new_coord['x'] -= 1

    elif direction == 'R':
        new_coord['x'] += 1

    return new_coord


def get_num_tail_visited(commands: list) -> int:
    visited = {'0,0': 1}  # k: 'x,y' v: visit count

    head = {'x': 0, 'y': 0}
    tail = {'x': 0, 'y': 0}

    for command in commands:
        for i in range(command['steps']):
            og_head = copy.deepcopy(head)

            head = move_coord(head, command['dir'])

            if not close_enough(head, tail):
                tail = og_head
                if str(tail['x']) + ',' + str(tail['y']) in visited:
                    visited[str(tail['x']) + ',' + str(tail['y'])] += 1
                else:
                    visited[str(tail['x']) + ',' + str(tail['y'])] = 1

    return len(visited)


# return coord that tail should use to properly follow head
def move_coord_to_follow(head: dict, tail: dict) -> dict:
    new_coord = copy.deepcopy(tail)

    if close_enough(head, tail):
        return new_coord

    # same x
    elif head['x'] == tail['x']:
        new_coord['y'] = (tail['y'] - 1, tail['y'] + 1)[head['y'] > tail['y']]

    # same y
    elif head['y'] == tail['y']:
        new_coord['x'] = (tail['x'] - 1, tail['x'] + 1)[head['x'] > tail['x']]

    # diff x and y
    else:
        new_coord['y'] = (tail['y'] - 1, tail['y'] + 1)[head['y'] > tail['y']]
        new_coord['x'] = (tail['x'] - 1, tail['x'] + 1)[head['x'] > tail['x']]

    return new_coord


def get_num_tail_visited_length_ten(commands: list) -> int:
    visited = {'0,0': 1}  # k: 'x,y' v: tail visit count

    snake = []
    for i in range(10):
        snake.append({'x': 0, 'y': 0})

    for command in commands:
        for s in range(command['steps']):

            # move head here
            snake[0] = move_coord(snake[0], command['dir'])

            for i in range(1, len(snake)):  # move rest of snake to follow in here

                snake[i] = move_coord_to_follow(snake[i-1], snake[i])

            # add tail to visited counter
            if str(snake[9]['x']) + ',' + str(snake[9]['y']) in visited:
                visited[str(snake[9]['x']) + ',' + str(snake[9]['y'])] += 1
            else:
                visited[str(snake[9]['x']) + ',' + str(snake[9]['y'])] = 1

    return len(visited)


print(get_num_tail_visited(commands))

print(get_num_tail_visited_length_ten(commands))
