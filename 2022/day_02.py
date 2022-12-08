# ==================================== PART 1 =================================== #

f = open('day_02.input', 'r')
rounds = f.readlines()
for i in range(len(rounds)):
    round_as_list = rounds[i].split(' ')
    translate = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissors',
    }
    rounds[i] = {
        'opp': translate[round_as_list[0]],
        'me': translate[round_as_list[1].strip()] # get rid of \n
    }

'''
format:
[
    {'me': 'A', 'opp': 'Y'},
    {'me': 'B', 'opp': 'X'},
    {'me': 'C', 'opp': 'Z'}
]
'''

def getScore(round: dict) -> int:
    move_score = {
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }
    # insert opp + me
    outcome_score = {
        'rockrock': 3,
        'rockpaper': 6,
        'rockscissors': 0,
        'paperrock': 0,
        'paperpaper': 3,
        'paperscissors': 6,
        'scissorsrock': 6,
        'scissorspaper': 0,
        'scissorsscissors': 3
    }

    return move_score[round['me']] + outcome_score[round['opp'] + round['me']]

total_score = 0
for r in rounds:
    total_score += getScore(r)

print(total_score)

# ==================================== PART 2 =================================== #

# format 
f = open('day_02.input', 'r')
rounds = f.readlines()
for i in range(len(rounds)):
    round_as_list = rounds[i].split(' ')
    translate = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win',
    }
    rounds[i] = {
        'opp': translate[round_as_list[0]],
        'outcome': translate[round_as_list[1].strip()] # get rid of \n
    }

'''
format:
[
    {'opp': 'scissors', 'outcome': 'win'},
    {'opp': 'scissors', 'outcome': 'win'},
    {'opp': 'scissors', 'outcome': 'win'}
]
'''

def getScore(round: dict) -> int:
    outcome_score = {
        'lose': 0,
        'draw': 3,
        'win': 6
    }
    # insert opp + me
    move_score = {
        'rocklose': 3,
        'rockdraw': 1,
        'rockwin': 2,
        'paperlose': 1,
        'paperdraw': 2,
        'paperwin': 3,
        'scissorslose': 2,
        'scissorsdraw': 3,
        'scissorswin': 1
    }

    return outcome_score[round['outcome']] + move_score[round['opp'] + round['outcome']]

total_score = 0
for r in rounds:
    total_score += getScore(r)

print(total_score)
