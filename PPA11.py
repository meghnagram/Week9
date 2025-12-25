def insert(L, x):
    """
    Insert x in L

    Parameters:
        L: list of sorted integers
        x: integer
    Return:
        result: sorted list of integers
    """
    c=len(L)
    for i in range(len(L)):
        if x<L[i]:
            c=i 
            break
    L.insert(c,x)
    return L

def isort(L,c=0):
    """
    A recursive function to sort the list L

    Arguments:
        L: list of integers
    Return:
        result: sorted list of integers
    """
    
    M=insert(L[0:c+1],L[c+1])
    if len(M)==len(L):
        return M
    else:
        return(isort(M+L[len(M):],c+1))
    
            
        
