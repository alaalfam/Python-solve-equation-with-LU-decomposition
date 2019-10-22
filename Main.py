import Util
import Equation


def read_matrix(n):
    matrix_a = []
    for i in range(n):
        print("Enter row: ", i)
        matrix_a.append(input().split())
    matrix_a = Util.convert_matrix_element_to_float(matrix_a)
    return matrix_a


def read_vector(n):
    vector_a = input().split()
    vector_a = Util.convert_vector_element_to_float(vector_a)
    if len(vector_a) != n:
        return False
    return vector_a


def main():
    n = input("Enter number of row.")
    n = int(n)

    matrix_a = read_matrix(n)
    print("Enter result vector:")
    vector_result = read_vector(n)
    if vector_result == False:
        print("Number of element should be : ", n)
        return
    matrix_x = Equation.solve_equation(matrix_a, vector_result)


main()
