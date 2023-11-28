import random
import string

# char = random.choice("0123456789")
# print(char)
#
# print(string.ascii_lowercase)  # "abcdefghijklmnopqrstuvwxyz"
# print(string.ascii_uppercase)  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(string.digits)  # "0123456789"
#
# all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
# print("all_chars:", all_chars)
#
# random_char = random.choice(all_chars)
# print("random_char:", random_char)


# s = ""
# for i in range(5):
#     s += str(i)
# print(s)
#随机字符串
s = ""
for i in range(5):
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    # print("all_chars:", all_chars)
    random_char = random.choice(all_chars)
    s += random_char
print(s)



