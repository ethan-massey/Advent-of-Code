class WordSearch:
    def __init__(self, data_filename):
        self.__rows = self.__read_data_into_rows(data_filename)
        self.__length = len(self.__rows[0])
        self.__height = len(self.__rows)

    def __read_data_into_rows(self, filename):
        ret = []
        lines = open(filename, 'r').readlines()
        for line in lines:
            line_chars = list(line.strip())
            ret.append(line_chars)
        return ret

    # done
    def __get_num_horizontal_matches(self, word):
        num_matches = 0
        for r in range(self.height):
            for c in range(self.length - len(word) + 1):
                current_segment = ''.join(self.rows[r][c:c + len(word)])
                if self.__is_string_equal(current_segment, word):
                    num_matches += 1
        return num_matches

    def __get_num_vertical_matches(self, word):
        num_matches = 0
        for r in range(self.height - len(word) + 1):
            for c in range(self.length):
                relevant_rows = self.rows[r:r + len(word)]
                current_segment = ''.join([row[c] for row in relevant_rows])
                if self.__is_string_equal(current_segment, word):
                    num_matches += 1
        return num_matches

    def __get_num_diagonal_L_to_R_matches(self, word):
        num_matches = 0
        for r in range(self.height - len(word) + 1):
            for c in range(self.length - len(word) + 1):
                current_segment = self.__get_diagonal_segment('L_to_R', r, c, len(word))
                if self.__is_string_equal(current_segment, word):
                    num_matches += 1
        return num_matches

    def __get_num_diagonal_R_to_L_matches(self, word):
        num_matches = 0
        for r in range(self.height - len(word) + 1):
            for c in range(len(word) - 1, self.length):
                current_segment = self.__get_diagonal_segment('R_to_L', r, c, len(word))
                if self.__is_string_equal(current_segment, word):
                    num_matches += 1
        return num_matches

    def __get_diagonal_segment(self, direction, row, column, length):
        r = row
        c = column
        segment = ''
        for i in range(length):
            segment += self.rows[r][c]
            r += 1
            if direction == 'L_to_R':
                c += 1
            elif direction == 'R_to_L':
                c -= 1
        return segment

    # return if strings are equal forward or reversed
    def __is_string_equal(self, str1, str2):
        return str1 == str2 or str1[::-1] == str2

    def get_num_occurrence(self, word):
        total = 0
        total += self.__get_num_horizontal_matches(word)
        total += self.__get_num_vertical_matches(word)
        total += self.__get_num_diagonal_L_to_R_matches(word)
        total += self.__get_num_diagonal_R_to_L_matches(word)
        return total

    def get_num_x_mases(self):
        mas = 'MAS'
        total = 0
        for r in range(self.height - len(mas) + 1):
            for c in range(self.length - len(mas) + 1):
                l_to_r_segment = self.__get_diagonal_segment('L_to_R', r, c, 3)
                if self.__is_string_equal(l_to_r_segment, 'MAS'):
                    r_to_l_segment = self.__get_diagonal_segment('R_to_L', r, c + 2, 3)
                    if self.__is_string_equal(r_to_l_segment, 'MAS'):
                        total += 1
        return total

    @property
    def rows(self):
        return self.__rows

    @property
    def length(self):
        return self.__length

    @property
    def height(self):
        return self.__height
