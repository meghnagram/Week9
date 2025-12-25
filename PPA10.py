def search(L, k):
    """
    A recursive function that searches for an element k in L.

    Parameters:
    	L: list
    	k: int
    Return:
    	bool
    """
    if len(L) ==1:
        if L[0]==k:
            return True
        else:
            return False
    else:
        return (L[0]==k or search(L[1::],k) )
    
    
