from os import mkdir
from os.path import exists

number_of_tasks = 25
main_file_name = '__main__.py'
data_file_name = 'data.txt'


def create_file(path_file):
    try:
        if not exists(path_file):
            with open(path_file, 'w') as new_file:
                pass
    except IOError as error:
        print(error)
    except BaseException as error:
        print(error)


if __name__ == '__main__':
    for num in range(1, number_of_tasks + 1):  # 0..25
        dir_name = f'{num}'
        if not exists(dir_name):
            mkdir(dir_name)

            main_path = '\\'.join((dir_name, main_file_name))
            create_file(main_path)

            data_path = '\\'.join((dir_name, data_file_name))
            create_file(data_path)
