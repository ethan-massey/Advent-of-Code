f = open('day_04.input', 'r')
elf_pairs = f.readlines()
for i in range(len(elf_pairs)):
    pair = elf_pairs[i].split(',')
    e1 = pair[0].split('-')
    e2 = pair[1].split('-')
    elf_pairs[i] = {
        'elf1': {
            'min' : int(e1[0]),
            'max' : int(e1[1]),
        },
        'elf2': {
            'min' : int(e2[0]),
            'max' : int(e2[1])
        }
    }

# ======================= PART 1 ================================= #

def isFullyOverlappingPair(e1, e2) -> bool:
    if e1['min'] <= e2['min'] and e1['max'] >= e2['max']:
        return True
    elif e2['min'] <= e1['min'] and e2['max'] >= e1['max']:
        return True
    return False

num_overlapping = 0
for p in elf_pairs:
    if isFullyOverlappingPair(p['elf1'], p['elf2']):
        num_overlapping += 1

print(num_overlapping)

# ======================= PART 2 ================================= #

# find greatest min and other's max. if min > max, not overlapping
def isOverlappingPair(e1, e2) -> bool:
    greater_min_elf = None
    if e1['min'] >= e2['min']:
        greater_min_elf = e1
        other_elf = e2
    else:
        greater_min_elf = e2
        other_elf = e1
    if greater_min_elf['min'] <= other_elf['max']:
        return True

    return False

num_overlapping = 0
for p in elf_pairs:
    if isOverlappingPair(p['elf1'], p['elf2']):
        num_overlapping += 1

print(num_overlapping)
