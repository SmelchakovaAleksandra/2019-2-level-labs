

def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    matrix = []
    if (num_rows and num_cols) and all(isinstance(i, int) for i in [num_cols, num_rows]) and (num_rows, num_cols != 0, 0):
        matrix = [[0] * num_cols for i in range(num_rows)]
    return matrix


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if list(edit_matrix) == [] or [] in edit_matrix or (type(add_weight) != int or type(remove_weight) != int):
        return list(edit_matrix)
    else:
        pr_ij = 0
        for i in range(len(edit_matrix)):
            if i == 0:
                continue
            else:
                edit_matrix[i][0] = pr_ij + remove_weight
                pr_ij = int(edit_matrix[i][0])
        pr_ij = 0
        for j in range(len(edit_matrix[0])):
            if j == 0:
                continue
            else:
                edit_matrix[0][j] = pr_ij + add_weight
                pr_ij = int(edit_matrix[0][j])
                print(edit_matrix)
        print(edit_matrix)
    return list(edit_matrix)


def minimum_value(numbers: tuple) -> int:
    res = min(numbers)
    return res


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    if not edit_matrix or [] in edit_matrix:
        return list(edit_matrix)
    if not all(isinstance(i, int) for i in [add_weight, remove_weight, substitute_weight]):
        return list(edit_matrix)
    if not all(isinstance(i, str) for i in [original_word, target_word]):
        return list(edit_matrix)
    for i in range(1, (len(edit_matrix))):
        for j in range(1, (len(edit_matrix[0]))):
            min_i, min_j, min_ij = 100, 100, 100
            min_i = edit_matrix[i - 1][j] + remove_weight
            min_j = edit_matrix[i][j - 1] + add_weight
            if j <= len(edit_matrix):
                if original_word[i - 1] != target_word[j - 1]:
                    min_ij = edit_matrix[i - 1][j - 1] + substitute_weight
                else:
                    min_ij = edit_matrix[i - 1][j - 1]
            edit_matrix[i][j] = minimum_value((min_i, min_j, min_ij))
    return list(edit_matrix)


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if not all(isinstance(i, str) for i in [original_word, target_word]):
        return -1
    if not all(isinstance(i, int) for i in [add_weight, remove_weight, substitute_weight]):
        return -1
    matrix = generate_edit_matrix(len(original_word) + 1, len(target_word) + 1)
    initialize_edit_matrix(matrix, add_weight, remove_weight)
    fill_edit_matrix(matrix, add_weight, remove_weight, substitute_weight, original_word, target_word)
    res = matrix[-1][-1]
    return res

def save_to_csv(edit_matrix, path_to_file):
    file = open(path_to_file, 'w')
    for i in list(edit_matrix):
        file.write('%s\n' % ','.join(str(j) for j in i))
    file.close()
    return None

def load_from_csv(path_to_file):
    file = open(path_to_file, 'r')
    res = []
    for l in file:
        k = l.strip()
        res.append(k.split(','))
    file.close()
    return res


