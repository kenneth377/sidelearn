# # # # # # # f = open('ll.txt',"r+")

# # # # # # # f.write("Hello I am\n A good one too")

# # # # # # # print(str(f.readline()))

# # # # # # # f.close()

# # # # # # with open("ll.txt","r+") as f:
# # # # # #     for line in f:
# # # # # #         # print(f.readline().rstrip())
# # # # # #         print(f.read())


# # # # # def read_file(filename=""):
# # # # #     with open(filename, "r") as f:
# # # # #         print(f.read())

# # # # # read_file("ll.txt")


# # # # def write_file(filename="", text=""):
# # # #     with open(filename,"w") as f:
# # # #         f.write(text)


# # # # nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
# # # # print(nb_characters)


# # # def append_write(filename="", text=""):
# # #     with open(filename,"a") as f:
# # #         f.write(text)


# # # nb_characters_added = append_write("file_append.txt", "This School is still so cool!\n")
# # # print(nb_characters_added)


# # import json

# # def to_json_string(my_obj):
# #     return json.dumps(my_obj)

# # my_list = [1, 2, 3]
# # s_my_list = to_json_string(my_list)
# # print(s_my_list)
# # print(type(s_my_list))

# # my_dict = { 
# #     'id': 12,
# #     'name': "John",
# #     'places': [ "San Francisco", "Tokyo" ],
# #     'is_active': True,
# #     'info': {
# #         'age': 36,
# #         'average': 3.14
# #     }
# # }
# # s_my_dict = to_json_string(my_dict)
# # print(s_my_dict)
# # print(type(s_my_dict))

# # try:
# #     my_set = { 132, 3 }
# #     s_my_set = to_json_string(my_set)
# #     print(s_my_set)
# #     print(type(s_my_set))
# # except Exception as e:
# #     print("[{}] {}".format(e.__class__.__name__, e))

# import json


# def save_to_json_file(my_obj, filename):
#     with open(filename,"w") as f:
#         f.write(json.dumps(my_obj))

# filename = "my_list.json"
# my_list = [1, 2, 3]
# save_to_json_file(my_list, filename)

# filename = "my_dict.json"
# my_dict = { 
#     'id': 12,
#     'name': "John",
#     'places': [ "San Francisco", "Tokyo" ],
#     'is_active': True,
#     'info': {
#         'age': 36,
#         'average': 3.14
#     }
# }
# save_to_json_file(my_dict, filename)

# try:
#     filename = "my_set.json"
#     my_set = { 132, 3 }
#     save_to_json_file(my_set, filename)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))