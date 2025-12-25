def count(L, word):
    """
    A recursive function to compute the frequency of occurrences of word in L.

    Parameters:
        L: list of words
        word: string
    Return:
        result: integer
    """
    if word==L[0]:
        c=1
    else:
        c=0
        
    if len(L)==1:
        return(c)
    else:
        return (c+count(L[1::],word))
