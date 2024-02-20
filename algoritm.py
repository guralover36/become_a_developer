# Для запуску програми знадобиться Python, його можливо завантажити на - "python.org/downloads/"
# Також у консолі потрібно написати - "pip install requirements.txt", щоб встановити залежності.
# Для запуску - "python algoritm.py" також у консолі.


import numpy as np
import time

def process_large_file(file_path):
    start_time = time.time()

    with open(file_path, 'r') as file:
        values = list(map(int, file))

    # 1. максимальне число в файлі;
    max_val = max(values)
    # 2. мінімальне число в файлі;
    min_val = min(values)

    total_sum = sum(values)

    # 3. знаходження медіани;
    median = np.percentile(values, 50)

    # 5 && 6 найбільша та найменша послідовність;
    current_max_sequence = current_min_sequence = [values[0]]
    max_sequence = min_sequence = [values[0]]

    for value in values[1:]:
        if value >= current_max_sequence[-1]:
            current_max_sequence.append(value)
        else:
            current_max_sequence = [value]

        if value <= current_min_sequence[-1]:
            current_min_sequence.append(value)
        else:
            current_min_sequence = [value]

        if len(current_max_sequence) > len(max_sequence):
            max_sequence = current_max_sequence.copy()

        if len(current_min_sequence) > len(min_sequence):
            min_sequence = current_min_sequence.copy()

    # 4. середнє арифметичне значення;
    average = total_sum / len(values)

    end_time = time.time()
    execution_time = end_time - start_time

    return max_val, min_val, median, average, max_sequence, min_sequence, execution_time

file_path = 'numbers.txt'
result = process_large_file(file_path)

print(f"Максимальне число: {result[0]}")
print(f"Мінімальне число: {result[1]}")
print(f"Медіана: {result[2]}")
print(f"Середнє арифметичне: {result[3]}")
print(f"Найбільша зростаюча послідовність: {result[4]}")
print(f"Найбільша спадна послідовність: {result[5]}")
print(f"Час виконання: {result[6]} секунд")
