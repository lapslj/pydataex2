def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'i': 1, 'o': 2, 'a': 3, 'e': 2, 'u': 1}
    """

    lowerphrase = phrase.lower()
    vcount = {}
    phrase_just_vowels = {ltr.lower() for ltr in phrase if ltr in "aeiouAEIOU"}
    
    for ltr in phrase_just_vowels:
        vcount[ltr] = lowerphrase.count(ltr)
    #print(vcount)
    return vcount
    
