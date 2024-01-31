# def magic_string(iteration=[0]):
#     iteration[0] += 1
#     return "BestSchool" * iteration[0]

# for i in range(10):
#     print(magic_string())


# class LockedClass:
#     __slots__ = ['first_name']

# lc = LockedClass()
# lc.first_name = "John"
# try:
#     lc.last_name = "Snow"
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

    
def magic_string():
    magic_string.iteration = getattr(magic_string, "iteration",0) +1
    return ("BestSchool, " * (magic_string.iteration - 1) + "BestSchool")

for i in range(10):
    print(magic_string())