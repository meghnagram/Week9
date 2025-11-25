def collatz(n):
    """
    A recursive function to compute the number of calls to the Collatz function of n

    Argument:
        n: integer
        Assume that 1 < n <= 32,000
    Returns: 
        result: integer
    """
    
    if n%2==0:
        f=n//2 
    else:
        f=3*n+1
    
    if f==1:
        return 1
    else:
        return(1+collatz(f))
