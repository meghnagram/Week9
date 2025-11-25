def ancestry(P, present, past):
    """
    A recursive function to compute the sequence of ancestors of person

    Arguments:
        P: dict, key and value are strings
        present: string
        past: string
    Return:
        result: list of strings
    """
    
    if P[present]==past:
        return [present]+[past]
    else:
        newpresent=P[present]
        return([present]+ancestry(P,newpresent,past))
