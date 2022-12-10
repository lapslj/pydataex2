def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    words = phrase.lower().split()
    j = 0
    while j < len(words):
        word = words[j]
        i = 0
        newfirst = ""
        while i < len(word):
            ltr = word[i].upper() if i == 0 else word[i]
            newfirst += ltr
            i += 1
        words[j] = newfirst
        j += 1
    out=words
    return " ".join(out)