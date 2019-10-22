import Decomposition


def solve_equation(matrix_a, vector_result):
    p, l, u = Decomposition.decompose_lu(matrix_a)

    matrix_y = calculate_y(l, vector_result)
    matrix_x = calculate_x(matrix_y, u)
    print("L :")
    print(l)
    print("U :")
    print(u)
    print("matrix_y :")
    print(matrix_y)
    print("matrix_x :")
    print(matrix_x)
    return matrix_x


def calculate_x(matrix_y, u):
    """
    UX = Y
    :param matrix_y: calculate from LY = R
    :param u: upper triangle
    :return: X
    """
    matrix_x = [0.0 for i in range(len(matrix_y))]
    n = len(matrix_y)
    matrix_x[n - 1] = matrix_y[n - 1] / u[n-1][n-1]
    for i in range(n - 2, -1, -1):
        c = 0
        for j in range(i + 1, n):
            c += u[i][j] * matrix_x[j]
        matrix_x[i] = (matrix_y[i] - c) / u[i][i]
    return matrix_x


def calculate_y(l, vector_result):
    """
    LUX = R -> let UX = Y -> LY = R

    :param l: lower triangle
    :param vector_result: AX = R , R is vector_result
    :return: Y
    """
    matrix_y = [0.0 for i in range(len(vector_result))]
    matrix_y[0] = vector_result[0]
    for i in range(1, len(vector_result)):
        c = 0
        for j in range(i):
            c += l[i][j] * matrix_y[j]
        matrix_y[i] = (vector_result[i] - c)
    return matrix_y
