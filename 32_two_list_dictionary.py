def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    #create tuples of vals and keys
    i = 0
    tuple_list = []
    while i < len(keys):
        value = values[i] if i < len(values) else None
        tuple_list.append([keys[i],value])
        i += 1
    res = dict(tuple_list)
    # i = 0
    # while i <= len(keys):
    #     res.keys[i] = values[i]
    #     i += 1
    return res

#print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))
