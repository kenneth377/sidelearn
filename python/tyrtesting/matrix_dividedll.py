

def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        for i in matrix:
            if not isinstance(i, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            elif len(i) != len(matrix[0]):
                    raise TypeError("Each row of the matrix must have the same size")
            else:
                for j in i:
                    if type(j) not in [int, float]:
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    
    elif div == 0:
        raise ZeroDivisionError("division by zero")
                    
    return [[round((j/div),2) for j in v] for v in matrix]

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(matrix_divided(matrix, 1))
# print(matrix)