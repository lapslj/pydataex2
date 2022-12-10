def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    i = 0
    out = ""

    while i < len(phrase):
        ltr = phrase[i]
        ltr = ltr if i != 0 else ltr.swapcase()
        out += ltr
        i += 1
    
    return out