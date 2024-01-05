numbers = [1,3,5,2,7,8,9,0,4,6]

names = ["Kenneth", "leav", "Kee", "Peele"]

newnumbers = [item*2 for item in numbers if item %2 ==0]

newnames = [name.upper() for name in names]
print(newnumbers)
print(newnames)
