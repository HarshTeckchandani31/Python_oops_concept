# lst=[1,2,3,4,5]
# str = "intro to oops python"
# int_num=123

# # print(type(lst))
# # print(type(str))
# # print(type(int_num))

# lst.clear()
# str1=str.capitalize()
# print(str1)
# print(lst)

from oops_py_project import chatbook

# obj = chatbook()

# lst = [1,2,3]

# function
# a1= len(lst)
# print(a1)

# calling method
# user1 = chatbook()
# user1.msg_friend()

# getter setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())
user1 = chatbook()
print(user1.id)

# using static method directly from class rather than obj

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)