def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for thing in lst:
        if type(thing) == list:
            continue
        else:
            return False
    
    return True
