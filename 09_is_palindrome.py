from reversestring import reverse_string

def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    spaceless_phrase = [ltr for ltr in phrase if ltr != " "]
    concat_phrase = "".join(spaceless_phrase).lower()
    return reverse_string(concat_phrase) == concat_phrase