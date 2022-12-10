def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # swap_to = to_swap.lower() if to_swap.isupper else to_swap.upper()
    # phrase.replace(swap_to,to_swap)
    to_swap = to_swap.lower()
    output = ""
    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        output += ltr
    return output