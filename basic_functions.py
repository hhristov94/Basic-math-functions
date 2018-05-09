
"""
Basic linear algebra functions
"""
import math

def vector_add(x,y):
	"""adds the corresponding elements in the two vectors"""
	return [x_i + y_i for x_i, y_i in zip(x,y)]

def vector_substract(x,y):
	"""adds the corresponding elements in the two vectors"""
	return [x_i - y_i for x_i, y_i in zip(x,y)]

def dot_product(x,y):
	"""computes the dot product of the two vectors"""
	return sum(x_i * y_i for x_i, y_i in zip(x,y))

def squared_sum(x):
	"""v_1 * v_1 + ... + v_n * v_n"""
	return dot(x,x)

def l2_norm(x):
	return math.sqrt(squared_sum(x))

def euclidian_distance(x,y):
	return l2_norm(v_substract(x,y))

def make_matrix(n_rows,n_columns, entry_fn):
	"""returns a n_rows by n_cols matrix"""
	return [[entry_fn(i,j) for j in range(n_cols)] for i in range(n_rows)]

def diagonal_ones(i,j):
	return 1 if i==j else 0

def identity_matrix(n_rows,n_columns):
	return make_matrix(n_rows,n_columns,diagonal_ones)

def m_shape(A):
    n_rows = len(A)
    n_cols = len(A[0]) if A else 0
    return n_rows, n_cols

def get_column(A, j):
	return [A_i[j] for A_i in A]

def matrix_multiplication(A, B):
	"""returns the product of two matrices"""
    A_rows, A_cols = m_shape(A)
    B_rows, B_cols = m_shape(B)
    if A_cols != B_rows :
    	print("The number of columns and rows doesn't match.")
    else :
        return [[dot_product(A[i],get_column(B,j)) for j in range(B_cols)] for i in range(A_rows)]