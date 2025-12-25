def subset_sum(L, s):
    """
    A recursive function to determine the presence of a subset with sum s.

    Parameters:
        L: list of integers
        s: integer
    Return:
        result: bool
    """
    
    if s==0:
        return True
    if L==[]:
        return False
    
    return subset_sum(L[1::],s) or subset_sum(L[1::],s-L[0])
    
    
