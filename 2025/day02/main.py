def get_ranges():
    f = open('day02.txt', 'r')
    ranges = [s for s in f.readlines()[0].split(',')]
    parsed = []
    for r in ranges:
        parsed.append({'min': int(r.split('-')[0]), 'max': int(r.split('-')[1])})
    return parsed


def is_invalid_id(id: int) -> bool:
    str_id = str(id)
    first_half = str_id[:len(str_id)//2]
    second_half = str_id[len(str_id)//2:]
    return first_half == second_half


def process_id_ranges(ranges):
    invalid_ids = []
    for r in ranges:
        for i in range(r['min'], r['max'] + 1):
            if is_invalid_id(i):
                invalid_ids.append(i)
    return sum(invalid_ids)


def get_substrings(num: int, length: int):
    s = str(num)
    substrings = []
    for i in range(0, len(s), length):
        substrings.append(s[i:i+length])
    return substrings


def items_in_list_are_equal(lst):
    return all(x == lst[0] for x in lst)


# Algorithm:
# for each number in a range
#   for each substring length from 1 -> len(number)-1
#       if the number can be evenly divided into substrings of that length
#           get the substrings
#           if all substrings are equal
#               mark the number as invalid
def process_id_ranges_v2(ranges):
    invalid_ids = []
    for r in ranges:
        for i in range(r['min'], r['max'] + 1):
            for substring_length in range(len(str(i))-1, 0, -1):
                if len(str(i)) % substring_length == 0:
                    substrings = get_substrings(i, substring_length)
                    if items_in_list_are_equal(substrings):
                        invalid_ids.append(i)
                        break
    return sum(invalid_ids)


print(process_id_ranges(get_ranges()))
print(process_id_ranges_v2(get_ranges()))
