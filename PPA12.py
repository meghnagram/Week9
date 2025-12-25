def poly(L, x_0,c=0):
    """
    A recursive function to compute the value of a polynomial.

    Parameters:
        L: list of integers
        x_0: integer
    Return:
        result: integer
        
    """
    if len(L)==1:
        return(L[0]*(x_0**c))
        
    return(L[0]*(x_0**c)+poly(L[1::],x_0,c+1))
    
    
