numbers = [1,3,5,2,7,8,9,0,4,6]

firstnames = ["Kenneth", "leav", "Kee", "Peele"]
othernames = ["Kenneth", "shah", "Kee","jdjsj", "jewjew", "iadjajd", "jajladk", "ksak"]


newnumbers = [item*2 for item in numbers if item %2 ==0]

newnam = [name for name in othernames if name in firstnames]

newnames = [name.upper() for name in firstnames]
print(newnumbers)
print(newnames)
print(newnam)
