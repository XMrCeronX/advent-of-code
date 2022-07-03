if __name__ == '__main__':
    # --- Day 2: Dive! ---
    depth = 0
    horizontal_position = 0
    with open('data.txt', 'r') as data_file:
        for line in data_file.readlines():
            line_data = line.split(' ')
            command = line_data[0]
            number = int(line_data[1])
            if command in 'forward':
                horizontal_position += number
            elif command in 'down':
                depth += number
            else:  # up
                depth -= number
    result = depth * horizontal_position
    print(result)  # 1488669
    print()
    # --- Part Two ---
    depth = 0
    horizontal_position = 0
    aim = 0
    with open('data.txt', 'r') as data_file:
        for line in data_file.readlines():
            line_data = line.split(' ')
            command = line_data[0]
            number = int(line_data[1])
            if command in 'forward':
                horizontal_position += number
                depth += aim * number
            elif command in 'down':
                aim += number
            else:  # up
                aim -= number
    result = depth * horizontal_position
    print(result)  # 1176514794
