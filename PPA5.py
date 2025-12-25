def palindrome(word):
    """
    A recursive function to determine if a string is a palindrome.

    Parameters:
        word: string
    Return:
        result: bool
    """
    if len(word)<=1:
        return True
    else:
        if word[0]==word[-1]:
            l=word[1:-1:]
            if len(l)==0:
                return True
            return(palindrome(l))
        else:
            return False
    return True
        
