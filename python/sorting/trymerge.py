import math

lis = [4,6,2,1,7,8]

sortedarr = []
def mergesort(li):
    
    if(len(li)<2):
        print(li)
        return li
    
    mid = math.floor(len(li)/2)

    lefli = li[0:mid]
    righli = li[mid:]

    return merge(lefli, righli)

def merge(lefli,righli):
    newli = []
    mergesort(lefli)
    mergesort(righli)


print(mergesort(lis))