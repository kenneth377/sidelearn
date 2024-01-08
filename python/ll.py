# print("Hello")

# mylist = [1,2,3,4,5]


# def print_list_integer(li):
#     for i in li:
#         print("{}".format(i))

# print_list_integer(mylist)


# my_list = [1, 2, 3, 4, 5]

# def element_at(li,idx):
#     if  0 <= idx < len(li):
#         return li[idx]
#     return None

# print(len(my_list))
# print(element_at(my_list, 3))



# my_list = [1, 2, 3, 4, 5]

# def replace_in_list(li, idx, new_element):
#     if 0 < idx < len(li):
#         li[idx] = new_element
#     return li

# newlist = replace_in_list(my_list, 8, 19)

# print(newlist)
# print(my_list)



# my_list = [5242431,22, 543, 434, 456545,654,754, 121, 32242, 2342]


# def print_reversed_list_integer(my_list):
    
#     for i in range(len(my_list)):
#         print("{}".format(my_list[len(my_list) - i-1]))

# def print_reversed_list_integer(my_list):
#     for element in reversed(my_list):
#         print(element)

# print_reversed_list_integer(my_list)




# my_list = [1, 2, 3, 4, 5]

# def new_in_list(li, idx, new_element):
#     newl = li[:]
#     if 0< idx < len(li):
#         newl[idx] = new_element
#         return newl
#     return li

# newlist = new_in_list(my_list, 3, 19)

# print(newlist)
# print(my_list)





# str = "Chicago"

# def no_c(str):
#     newstr = ""
#     for i in str:
#         if i != "c" and  i != "C":
#             newstr += i
#     return newstr

#     print(newstr)
# no_c(str)
# print(str)




# matrixe = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# def print_matrix_integer(matrixi=[[]]):
#     if not matrixi:
#         return
#     for i in matrixi:
#         for j in i:
#             print("{}".format(j), end=" ")
#         print()
# print_matrix_integer(matrixe)
# print_matrix_integer()

# newmat = [[x[i] for i in range(len(x))] for x in matrixe] wrong
# newmat = [[x[i] for x in matrixe] for i in range(len(matrixe))] transposed
# print(newmat) 




# tuple_a = (1,)
# tuple_b = (1,)

# def add_tuple(a, b):
#     newt = ()
#     lena = 2 -len(a)
#     lenb = 2 -len(b)
#     if len(a)<2:
#         ze = 0,
#         a = (a+ ze*lena)
#         print(a)
#     if len(b)<2:
#         ze = 0,
#         b = (b + ze*lenb)
#         print(b)
#     else:
#         a = a[:2]
#         b = b[:2]

#     for i in range(2):
#         newv = a[i]+b[i]
#         newt =newt+(newv, )

#     return newt

# add_tuple(tuple_a,tuple_b)

# print(tuple_a,tuple_b)




# def multiple_returns(sentence):
#     newt = tuple(sentence)

#     return (len(newt),newt[0])
# sentence = "At school, I learnt C!"
# print(multiple_returns(sentence))


# def max_integer(my_list=[]):
#     maxnum= my_list[0]

#     for i in my_list:
#         if i>maxnum:
#             maxnum = i

#     return maxnum

# my_list = [1, 90, 2, 13, 34, 532, -13, 3]
# max_value = max_integer(my_list)
# print("Max: {}".format(max_value))





# def divisible_by_2(my_list=[]):
#     newlist = []

#     # for i in  range(len(my_list)):
#     #     newlist[i-1] = True if my_list[i-1]%2==0 else False

#     # for i in my_list:
#     #     newlist.append(True) if i%2==0 else newlist.append(False)

    # newlist =[True if my_list[i]% 2 == 0 else False for i in range(len(my_list))]

#     return newlist



# my_list = [0, 1, 2, 3, 4, 5, 6]
# print(divisible_by_2(my_list))


# def delete_at(my_list=[], idx=0):
#     if 0<= idx < len(my_list):
#         del my_list[idx]
#     return my_list

# my_list = [1, 2, 3, 4, 5]
# idx = 4
# new_list = delete_at(my_list, idx)
# print(new_list)
# print(my_list)


# !/usr/bin/python3
# a = 89
# b = 10
# a,b = b,a
# print("a={:d} - b={:d}".format(a, b))




# mylist = [1,5,6,4,3,8,9,4,6,7,6,1,2]

# def unique_elements(lst):
#     newlist =[]

#     for i in lst:
#         if i not in newlist:
#             newlist.append(i)
#         elif i in newlist:
#             newlist.pop(newlist.index(i))
            

#     return newlist
# print(unique_elements(mylist))


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12],
#     [13, 14, 15]
# ]

# def matrix_transpose(matrix):
#     for i in range(len(matrix)):
#         for row in matrix:
#             print(row[i], end =" ")
#         print()
        

# matrix_transpose(matrix)


# mixed_list = [1, ['hello'], [2, 3], 'world', [4, 'sublist', 5], 6]

# def count_sublists(lst):
#     sublist_count = 0
#     for i in lst:
#         if type(i) == list:
#             sublist_count+=1

#     return sublist_count

# print(count_sublists(mixed_list))

# list1 =[1,2,3,4,5,6]
# list2 = [2,3,5]

# def common_elements(list1, list2):
#     newlist = []
#     for i in list1:
#         for j in list2:
#             if j== i and i not in newlist:
#                 newlist.append(i)
#     return newlist

# print(common_elements(list1, list2))


# li = [1, [2, 3, [4, 5]], 6, [7, 8]]

# def flatten(lst):
#     newl = []

#     for i in lst:
#         if type(i) == list:
#             print(i)
#             newl.extend(flatten(i))
#         else:
#             newl.append(i)

#     return newl

# print(flatten(li))



# word = "abcba"

# def is_palindrome(word):
#     neww = "";

#     for i in range(len(word) - 1, -1, -1):
#         neww += word[i]
#     # for i in reversed(word):
#     #     neww+= i
    
#     if neww == word:
#         return True
#     else :
#         return False
# print(is_palindrome(word))



# list = [331,332,8985,66,342,8,9,54,21,34,54,22]

# def min_max_avg(lst):
#     min=  lst[0]
#     max = lst[0]
#     sum = 0
#     avg = 1

#     for i in lst:
#         if i>max:
#             max = i
#         if i<min:
#             min = i
        
#         sum += i

#     avg = sum / len(lst)

#     return(min, max, avg)


# print(min_max_avg(list))


# list = ["ken", "ss", "aa", "jj", "aa", "gf", "hjy","er"]

# def unique(lst):
#     newl = []

#     for i in lst:
#         if i not in newl:
#             newl.append(i)

#     return newl

# print(unique(list))



# list2 = [2,3,4,7,8,9,23,25]
# list1 = [5,10,15,18]

# def merge_sorted_lists(list1, list2):
#     for i in list2:
#         list1.append(i)

#     for i,iv in enumerate(list1):
#         for j, jv in enumerate(list1):
#             if iv<jv:
#                 list1[i],list1[j]=list1[j],list1[i]

#     return list1
# print(merge_sorted_lists(list1, list2))



# wordl = ["Ken", "neth", "osei", "tutu", "marfo", "set"]
# dicta ={}
# ll=[]
# lenl = []
# for i in wordl:
#     if len(i) not in lenl:
#         lenl.append(len(i))

# for i in lenl:
#     ll=[]
#     for j in wordl:
#         if len(j)== i:
#             ll.append(j)
#     dicta[i] = ll
# print(dicta)



nested_dict = {
    'person1': {
        'name': 'John',
        'age': 30,
        'address': {
            'city': 'New York',
            'zip_code': '10001'
        }
    },
    'person2': {
        'name': 'Alice', 
        'age': 25,
        'address': {
            'city': 'San Francisco',
            'zip_code': '94105'
        }
    }
}

# newdicta = {}
# kk =""

# def flatten_dict(dicta,newdicta,kk=""):
   
#     for i in dicta:
#         if type(dicta[i]) == dict:
#             flatten_dict(dicta[i],newdicta,"{}_{}".format(kk,i))
#         else:
#             newdicta["{}_{}".format(kk,i)] = dicta[i]
#     # print(newdicta)
#     return newdicta


# print(flatten_dict(nested_dict, newdicta,kk))

# newdict = {}

# def flat(dicta,newdict,sep=""):
    
#     for i,v in dicta.items():
#         if isinstance(v, dict):
#             # print(newdict)
#             flat(v,newdict, "{}{}".format(i,sep))
#         else:
#             newdict["{}{}".format(i,sep)]= v
#     return newdict
                
# print(flat(nested_dict,newdict))