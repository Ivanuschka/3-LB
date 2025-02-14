import numpy as np
import matplotlib.pyplot as plt

def is_valid_move(matrix, x, y, prev_char):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and ord(matrix[x][y]) == ord(prev_char) + 1

def longest_path(matrix, x, y, memo):
    if memo[x][y] is not None:
        return memo[x][y]
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),        (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    max_length = 1
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(matrix, new_x, new_y, matrix[x][y]):
            max_length = max(max_length, 1 + longest_path(matrix, new_x, new_y, memo))
    
    memo[x][y] = max_length
    return max_length

def find_longest_path(matrix, start_char):
    rows, cols = len(matrix), len(matrix[0])
    memo = [[None] * cols for _ in range(rows)]
    max_path = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == start_char:
                max_path = max(max_path, longest_path(matrix, i, j, memo))
    
    return max_path

# Создание случайной матрицы символов
np.random.seed(0)
letters = np.array([chr(i) for i in range(ord('A'), ord('Z') + 1)])
matrix = np.random.choice(letters, (5, 5))
print("Матрица символов:")
print(matrix)

start_char = 'A'
longest = find_longest_path(matrix, start_char)
print(f"Самый длинный путь в матрице, начиная с '{start_char}': {longest}")

# Визуализация матрицы
plt.figure(figsize=(6, 6))
plt.imshow(np.ones_like(matrix, dtype=int), cmap="coolwarm", interpolation="nearest")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        plt.text(j, i, matrix[i, j], ha='center', va='center', color='black')
plt.title("Матрица символов")
plt.show()
