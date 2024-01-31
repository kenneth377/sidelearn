def add(a, b):
    # """
    # >>> add(2, 7) #doctest: +NORMALIZE_WHITESPACE
    # 9
    # >>> add("a",5)
    # Traceback (most recent call last):
    # TypeError: here is the error
    # """
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("here is the error") 

    return int(a)+int(b)

add(2,3)