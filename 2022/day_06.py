f = open('day_06.input', 'r')
data = f.readlines()[0]

# return (index where current and last 3 letters
# are unique) + 1
def getMarker(data: str, unique_length_needed) -> int:
    char_tracker = {}
    i_tracker = {}

    for i in range(len(data)):
        if len(char_tracker) == unique_length_needed:
            return i
        if data[i] not in char_tracker:
            char_tracker[data[i]] = i
            i_tracker[i] = data[i]
        else:
            bad_index = char_tracker[data[i]]
            while bad_index in i_tracker:
                # delete from both
                del char_tracker[i_tracker[bad_index]]
                del i_tracker[bad_index]
                # add latest
                char_tracker[data[i]] = i
                i_tracker[i] = data[i]
                bad_index -= 1


print(getMarker(data, 4))
print(getMarker(data, 14))
