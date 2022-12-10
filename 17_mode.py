def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    value_set = set(nums)
    curr_mode = 0
    curr_count = 0
    for num in value_set:
        if nums.count(num) > curr_count:
            curr_mode = num
            curr_count = nums.count(num)
    return curr_mode
