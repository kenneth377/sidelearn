# def add(a,b):
#     """
#     Adds two numbers
#     >>> add(3,1)
#     4
#     >>> add(4,5)
#     9
#     """
#     return a+b


# print(add(3,1))
# print(add(4,5))


#ELLIPSIS

class Anyclass:
    pass

def tryer(obj):
    """
    >>> tryer(Anyclass()) #doctest: +ELLIPSIS
    <doctestll.Anyclass object at 0x...>
    """

    return obj


if __name__ == '__main__':
    import doctest
    doctest.testmod()