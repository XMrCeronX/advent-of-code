PATH_TO_FILE = 'data.txt'
FILE_MODE = 'r'


class Board:
    def __init__(self, board_str):
        self.__board = []
        self.__mark_board = []
        self.__parse_board_str(board_str)
        self.__create_mark_board()

    def __str__(self):
        result = ''
        for row in self.__board:
            for number in row:
                result += f'{number:3d}'  # '%3d' % number
            result += '\n'
        return result

    def __parse_board_str(self, board_str):
        for line in board_str.split('\n'):
            number_of_list = list(filter(lambda number: number != '', line.strip().split(' ')))
            number_of_list = list(map(int, number_of_list))
            self.__board.append(number_of_list)

    def __create_mark_board(self):
        mark_board = [False for i in range(len(self.__board))]
        for row in self.__board:
            self.__mark_board.append(mark_board.copy())

    def __update_mark_board(self, update_number):
        is_updated = False
        row_index = 0
        while len(self.__board) > row_index and not is_updated:
            row = self.__board[row_index]
            column_index = 0
            while len(row) > column_index and not is_updated:
                number = row[column_index]
                if number == update_number:
                    self.__mark_board[row_index][column_index] = is_updated = True
                column_index += 1
            row_index += 1

    def get_sum_all_unmarked_numbers(self):
        result = 0
        for row_index, row in enumerate(self.__board):
            for column_index, number in enumerate(row):
                if not self.__mark_board[row_index][column_index]:
                    result += number
        return result

    def __get_column(self, column_index):
        column = []
        for row in self.__mark_board:
            column.append(row[column_index])
        return column

    def is_bingo(self, number):
        self.__update_mark_board(number)

        for row in self.__mark_board:
            if all(row):
                return True

        for column_index, row in enumerate(self.__mark_board):
            if all(self.__get_column(column_index)):
                return True

        return False


class BingoSubsystem:
    def __init__(self):
        self.__result = 0
        self.__sequence_of_numbers = []
        self.__boards = []
        self.__parse_file_data()
        self.__calculate_result()

    def __str__(self):
        return f'{self.__result}'

    def __calculate_result(self):
        for number in self.__sequence_of_numbers:
            for board in self.__boards:
                if board.is_bingo(number):
                    self.__result = number * board.get_sum_all_unmarked_numbers()
                    return

    def get_last_winning_board(self):
        result = []
        for number in self.__sequence_of_numbers:
            board_index = 0
            while len(self.__boards) > board_index:
                board = self.__boards[board_index]
                if board.is_bingo(number):
                    sum_all_unmarked_numbers = number * board.get_sum_all_unmarked_numbers()
                    result.append(sum_all_unmarked_numbers)
                    self.__boards.remove(board)
                    board_index -= 1
                board_index += 1
        return result[-1]

    def __parse_list_of_numbers(self, file_data):
        self.__sequence_of_numbers = list(map(int, file_data[0].split(',')))

    def __parse_boards(self, file_data):
        for board_str in file_data[1:]:
            self.__boards.append(Board(board_str))

    def __parse_file_data(self):
        file_data = self.__get_file_data()
        self.__parse_list_of_numbers(file_data)
        self.__parse_boards(file_data)

    @staticmethod
    def __get_file_data():
        with open(PATH_TO_FILE, FILE_MODE) as file:
            data = file.read().split('\n\n')
        return data

    def print_boards(self):
        for board in self.__boards:
            print(board)


if __name__ == '__main__':
    # --- Day 4: Giant Squid ---
    bingo_subsystem = BingoSubsystem()
    # bingo_subsystem.print_boards()
    print(bingo_subsystem)  # 58374
    print()
    # --- Part Two ---
    print(bingo_subsystem.get_last_winning_board())  # 11377
