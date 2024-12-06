def multiply(*multiplicands):
    """
    Multiple values together from left to right. 
    If the types of the arguments are not compatible for multiplication, 
    a TypeError is raised.
    Returns 1 if no arguments were passed.
    """
    result = 1 # multiplicative unit
    for i, multiplicand in enumerate(multiplicands):
        if i == 0:
            result = multiplicand
        else: 
            try: 
                result *= multiplicand
            except:
                raise TypeError("Innapropiate multiplicand types.")
    return result
