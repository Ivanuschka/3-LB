import numpy as np
import matplotlib.pyplot as plt

def is_valid_move(matrix, x, y, visited):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and not visited[x][y]

def find_words(matrix, x, y, visited, current_word, word_list, dictionary):
    visited[x][y] = True
    current_word += matrix[x][y]
    
    if current_word in dictionary:
        word_list.add(current_word)
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),        (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(matrix, new_x, new_y, visited):
            find_words(matrix, new_x, new_y, visited, current_word, word_list, dictionary)
    
    visited[x][y] = False

def find_all_words(matrix, dictionary):
    rows, cols = len(matrix), len(matrix[0])
    word_list = set()
    visited = [[False] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            find_words(matrix, i, j, visited, "", word_list, dictionary)
    
    return word_list

# Создание матрицы, содержащей точно 10 слов из словаря
dictionary = {"CAT", "DOG", "BAT", "RAT", "CAR", "BAR", "ART", "TOOL", "TREE", "BIRD"}
matrix = np.array([
    ['C', 'A', 'T', 'O', 'X'],
    ['D', 'O', 'G', 'B', 'A'],
    ['B', 'A', 'T', 'R', 'A'],
    ['T', 'R', 'E', 'E', 'L'],
    ['B', 'I', 'R', 'D', 'Y']
])
print("Матрица символов:")
print(matrix)

found_words = find_all_words(matrix, dictionary)
print("Найденные слова:", found_words)

# Визуализация матрицы
plt.figure(figsize=(6, 6))
plt.imshow(np.ones_like(matrix, dtype=int), cmap="coolwarm", interpolation="nearest")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        plt.text(j, i, matrix[i, j], ha='center', va='center', color='black')
plt.title("Матрица символов")
plt.show()