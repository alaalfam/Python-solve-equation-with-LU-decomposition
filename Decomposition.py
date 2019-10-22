from scipy.linalg import lu
import numpy as np
import Util


def decompose_lu(matrix):
    matrix = np.array(matrix)
    p, l, u = lu(matrix)
    p = Util.convert_matrix_element_to_float(p)
    l = Util.convert_matrix_element_to_float(l)
    u = Util.convert_matrix_element_to_float(u)
    return p, l, u
