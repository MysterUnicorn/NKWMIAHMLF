def add(*addands):
    """
    Adds multiple values together from left to right. 
    If the types of the arguments are not compatible for addition, 
    a TypeError is raised.
    Returns 0 if no arguments were passed.
    """
    result = 0 # additive unit
    for i, addand in enumerate(addands):
        if i == 0:
            result = addand
        else: 
            try: 
                result += addand
            except:
                raise TypeError("Innapropiate addand types.")
    return result
