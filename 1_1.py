def euclid(first, second):
    """Returns the greatest common denominator of two numbers, naive implementation"""
    remainder = first % second
    if remainder == 0:
        return second

    first, second = second, remainder
    return euclid(first, second)

assert euclid(119, 544) == 17


def rearrange_assingment(first, second, third, fourth):
    """Rearrange the provided values so that first comes last, and pushes the rest forward, using temporary variable"""
    temporary = first
    first = second
    second = third
    third = fourth
    fourth = temporary
    return (first, second, third, fourth)


def rearrange_swap(first, second, third, fourth):
    """Rearrange the provided values so that first comes last, and pushes the rest forward, using swap assignment"""
    (first, second) = (second, first)
    (second, third) = (third, second)
    (third, fourth) = (fourth, third)
    return (first, second, third, fourth)


assert rearrange_assingment('a', 'b', 'c', 'd') == ('b', 'c', 'd', 'a')
assert rearrange_swap('a', 'b', 'c', 'd') == ('b', 'c', 'd', 'a')


def euclid(first, second):
    """Returns the greatest common denominator of two numbers without variable, 1_3 answer"""
    first = first % second
    if first == 0:
        return second

    second = second % first
    if second == 0:
        return first

    return euclid(first, second)

assert euclid(119, 544) == 17


def euclid_show_work(first, second):
    """Returns the greatest common denominator of two numbers without variable while showing work for 1_4"""
    first = first % second
    print(' > {}'.format(second))
    if first == 0:
        return second

    second = second % first
    print(' > {}'.format(first))
    if second == 0:
        return first

    return euclid_show_work(first, second)

assert euclid_show_work(2166, 6099) == 57


def euclid_calls(first, second, calls=1):
    """Returns the number of times a remainder is calculated"""
    remainder = first % second
    if remainder == 0:
        return calls

    first, second = second, remainder
    return euclid_calls(first, second, calls + 1)


assert sum([euclid_calls(value, 5) for value in range(1, 6)]) / 5 == 2.6
