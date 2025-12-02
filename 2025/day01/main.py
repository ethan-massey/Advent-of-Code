def get_rotation_list():
    f = open('day01.txt', 'r')
    rotations = [l.strip() for l in f.readlines()]
    return rotations


class Dial:

    def __init__(self):
        self.dial_location = 50
        self.times_hit_zero = 0
        self.times_passed_zero = 0

    def process_rotation_list(self, rotations):
        for rotation in rotations:
            self.rotate_dial(rotation)

    def rotate_dial(self, addend: str):
        int_addend = self.translate_addend(addend)

        # if addend >= 100 lets just process the extra turns here
        if abs(int_addend) >= 100:
            self.times_passed_zero += abs(int_addend) // 100
            int_addend = abs(int_addend) % 100 if int_addend >= 0 else - (abs(int_addend) % 100)

        # then process the remaining movement
        if self.dial_location != 0:
            if self.dial_location + int_addend > 99 or self.dial_location + int_addend <= 0:
                self.times_passed_zero += 1

        self.dial_location = (self.dial_location + int_addend) % 100
        if self.dial_location == 0:
            self.times_hit_zero += 1

    def translate_addend(self, addend: str) -> int:
        num = int(addend[1:])
        # make negative if needed
        num = 0 - num if addend[0] == 'L' else num
        return num


dial = Dial()
rotations = get_rotation_list()
dial.process_rotation_list(rotations)
print(dial.times_hit_zero)
print(dial.times_passed_zero)
