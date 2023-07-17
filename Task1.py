# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def matrix_transpose(input_matrix):
    new_matrix = []
    list_matrix = []
    count_start = 0
    count_stop = 1
    while count_start < len(matrix):
        for column in input_matrix:
            for row in column[count_start:count_stop:]:
                list_matrix.append(row)
        new_matrix.append(list_matrix)
        list_matrix = []
        count_start += 1
        count_stop += 1
    return new_matrix

print(matrix_transpose(matrix))