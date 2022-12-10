def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    digits1 = set(str1)
    digits2 = set(str2)
    # print(str1)
    # print(str2)
    counter1 = dict()
    counter2 = dict()

    for digit in digits1:
        counter1[digit] = counter1.get(str(digit),str1.count(digit))
    for digit in digits2:
        counter2[digit] = counter2.get(str(digit),str2.count(digit))
    
    # print(counter1)
    # print(counter2)

    return counter1 == counter2

same_frequency(1212, 2211)
