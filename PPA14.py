def det(M):
    """
    A recursive function to compute the determinant of M.
    
    Parameters:
        M: list of lists
    Return:
        result: integer
    """
    if len(M)==1:
        return(M[0])
    if len(M)==2:
        return(M[0][0]*M[1][1]-M[0][1]*M[1][0])
    if len(M)>=3:
        sum=0
        for i in range(len(M)):
            sum=sum+(-1)**i * M[0][i]*det(minor(M,i))
    return sum
def minor(M,a):
    s=[]
    l=[]
    for i in range(1,len(M)):
        for j in range(len(M)):
            if not( j==a):
                s.append(M[i][j])
        if len(s)!=0:
            l.append(s)
            s=[]
    return l
