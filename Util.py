def convert_matrix_element_to_float(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = float(matrix[i][j])
    return matrix


def convert_vector_element_to_float(vector):
    for i in range(len(vector)):
        vector[i] = float(vector[i])
    return vector
