def add(a,b):
    if a<0 or b<0:
        raise TypeError("Error: Number can not be less than zero ")
    return a+b