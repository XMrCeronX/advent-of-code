from collections import deque

if __name__ == '__main__':
    # --- Day 1: Sonar Sweep ---
    prev_number = None
    count_inc = 0
    with open('data.txt', 'r') as data_file:
        for line in data_file.readlines():
            current_number = int(line)
            if prev_number is not None and current_number > prev_number:
                count_inc += 1
            prev_number = current_number
    print(count_inc)  # 1791
    print()
    # --- Part Two ---
    deq = deque()
    prev_sum = None
    count_inc = 0
    with open('data.txt', 'r') as data_file:
        for line in data_file.readlines():
            deq.append(int(line))
            if len(deq) == 3:
                current_sum = sum(deq)
                if prev_sum is not None and current_sum > prev_sum:
                    count_inc += 1
                prev_sum = current_sum
                deq.popleft()
    print(count_inc)  # 1822
