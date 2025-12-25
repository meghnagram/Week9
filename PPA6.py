def spiral_iterative(left, right, n):
    """
    An iterative function to compute the x-coordinate of the nth arm of the spiral.

    Parameters:
        left: integer
        right: integer
        n: integer
    Return:
        result: float
    """
    for i in range(n):
        if i%2==0:
           left=left+(right-left)/2
        else:
            right=left+(right-left)/2
    if n%2==0:
        return(left)
    else:
        return(right)
    
def spiral_recursive(left, right, n,i=0):
    """
    An recursive function to compute the x-coordinate of the nth arm of the spiral

    Arguments:
        left: integer
        right: integer
        n: integer
    Return:
        result: float
    """
    if i%2==0:
           left=left+(right-left)/2
    else:
            right=left+(right-left)/2
    i+=1
    if i==n:
        if n%2==0:
            return(left)
        else:
            return(right)
    else:
        return(spiral_recursive(left, right, n,i))
        
        
        
