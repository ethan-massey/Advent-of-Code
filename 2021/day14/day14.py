import collections


# returns tuple of str list that is initial polymer
# and dictionary containing polymer template
def format_data(filename: str):
    lines = open(filename, "r").readlines()
    polymer = [c for c in lines[0].strip()]
    template = {c.split(' -> ')[0].strip(): c.split(' -> ')[1].strip() for c in lines[2:]}
    return polymer, template


def build_polymer(num_steps: int, polymer: list, template: dict) -> list:
    new_polymer = polymer
    # chars to insert into polymer
    to_add = []
    for step in range(num_steps):
        for i in range(len(new_polymer)-1):
            current_pair = ''.join(new_polymer[i:i+2])
            to_add.append(template[current_pair])

        new_polymer = zipper(new_polymer, to_add)
        to_add.clear()
        print('done with step', step+1)
    return new_polymer


def build_polymer_faster(num_steps: int, polymer: list, template: dict):
    print()

def zipper(polymer: list, to_add: list) -> list:
    new_list = []
    for i in range(len(polymer)-1):
        new_list.append(polymer[i])
        new_list.append(to_add[i])
    new_list.append(polymer[-1])
    return new_list


def main():
    results = format_data("data.txt")
    polymer = results[0]
    template = results[1]

    # Part 1
    polymer = build_polymer(10, polymer, template)
    occurrences = collections.Counter(polymer).most_common()
    print(occurrences[0][1] - occurrences[-1][1])

    # Part 2
    # occurrences = build_polymer_faster(40, polymer, template)
    # print(max(occurrences.values())-min(occurrences.values()))



if __name__ == '__main__':
    main()
