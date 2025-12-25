def non_decreasing(L):
    """
    A recursive function that determines if L is sorted in non-decreasing order.

    Parameters: 
        L: list of integers
    Return:
        result: bool
    """
    
    if L[0] <= L[1]:
        b=True
    else:
        b=False
        
    if len(L)==2:
        return b 
    else:
        return( b and non_decreasing(L[1::]))
        
    
    
