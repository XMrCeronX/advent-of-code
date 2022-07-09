from collections import Counter, deque

if __name__ == '__main__':
    # --- Day 3: Binary Diagnostic ---
    PATH_TO_FILE = 'data.txt'
    FILE_MODE = 'r'

    with open(PATH_TO_FILE, FILE_MODE) as data_file:
        LENGTH_NUMBER = len(data_file.readline().strip())
    NUMERAL_SYSTEM = 2
    gamma_rate_str = ''
    epsilon_rate_str = ''

    dictionaries = [{str(n): 0 for n in range(NUMERAL_SYSTEM)}
                    for i in range(LENGTH_NUMBER)]  # OR dictionaries = [{'0': 0, '1': 0} for i in range(length)]

    with open(PATH_TO_FILE, FILE_MODE) as data_file:
        for line in data_file.readlines():
            for index, digit in enumerate(line.strip()):
                dictionaries[index][digit] += 1

    for dict_ in dictionaries:
        gamma_rate_str += '1' if dict_['1'] > dict_['0'] else '0'
        epsilon_rate_str += '0' if dict_['1'] > dict_['0'] else '1'

    gamma_rate = int(gamma_rate_str, NUMERAL_SYSTEM)
    epsilon_rate = int(epsilon_rate_str, NUMERAL_SYSTEM)
    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)  # 2035764
    print()
    # --- Part Two ---
    data = deque()

    with open(PATH_TO_FILE, FILE_MODE) as data_file:
        for line in data_file.readlines():
            data.append(line.strip())

    data2 = data.copy()

    for index, digit in enumerate(gamma_rate_str):
        dictionaries = [{str(n): 0 for n in range(NUMERAL_SYSTEM)} for i in range(LENGTH_NUMBER)]
        for number in data2:
            for index_, digit_ in enumerate(number):
                dictionaries[index_][digit_] += 1

        if len(data2) == 1:
            break
        counter = 0
        while len(data2) > counter and len(data2) > 1:
            string_number = data2[counter]
            max_bit = '1' if dictionaries[index]['1'] >= dictionaries[index]['0'] else '0'
            if string_number[index] != max_bit:
                data2.remove(string_number)
                counter -= 1
            counter += 1

    string_number = data2.pop()
    oxygen_generator_rating = int(string_number, NUMERAL_SYSTEM)

    for index, digit in enumerate(gamma_rate_str):
        dictionaries = [{str(n): 0 for n in range(NUMERAL_SYSTEM)} for i in range(LENGTH_NUMBER)]
        for number in data:
            for index_, digit_ in enumerate(number):
                dictionaries[index_][digit_] += 1

        if len(data) == 1:
            break
        counter = 0
        while len(data) > counter and len(data) > 1:
            string_number = data[counter]
            min_bit = '0' if dictionaries[index]['1'] >= dictionaries[index]['0'] else '1'
            if string_number[index] != min_bit:
                data.remove(string_number)
                counter -= 1
            counter += 1

    string_number = data.pop()
    scrubber_rating = int(string_number, 2)

    life_support_rating = oxygen_generator_rating * scrubber_rating
    print(life_support_rating)  # 2817661
