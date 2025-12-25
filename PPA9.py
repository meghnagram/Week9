def uniq(L):
    """
    A recursive function to get unique elements from the list.
    
    Parameters:
        L: list
    Return:
        result: list
    """
    b=[]
    if len(L)==1:
        return [L[0]]
    else:
        if L[0] not in L[1::]:
            return([L[0]]+uniq(L[1::]))
        else:
            return(uniq(L[1::]))
            
      
