def power(A, m):
    """
    A recursive function to compute A ** m.

    Parameters:
        A: list of lists
        m: integer
    Return:
        result: list of lists
    """
    if m == 1:
        return A

    half = power(A, m // 2)
    result = multiply(half, half)
    
    if m % 2 == 1:
        result = multiply(result, A)

    return result


def multiply(A, B):
    """
    Multiplies two square matrices A and B.
    """
    n = len(A)
    C = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C
    
    
    
