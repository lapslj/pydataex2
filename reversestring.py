def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    word_as_list = list(phrase)
    word_as_list.reverse()
    return "".join(word_as_list)

