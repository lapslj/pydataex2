def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    dims = len(matrix[1])
    # print(f"length is {dims}")
    sum = 0
    #TL to BR
    for i in range(dims): #for every row
        for j in range(dims): #within each row column by column
            adder = matrix[i][j] if i == j else 0
            sum += adder
    #flip the matrix
    for i in range(dims):
        matrix[i].reverse()
    # print(matrix)
    #do it again
    for i in range(dims): #for every row
        for j in range(dims): #within each row column by column
            adder = matrix[i][j] if i == j else 0
            sum += adder
    return sum


m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(sum_up_diagonals(m2))