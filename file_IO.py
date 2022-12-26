# MODE
# read        "r"
# write       "w"
# append      "a"
# readWrite   "r+"

file_1 = open("writefile.txt", "w")
file_1.write("hi this is demo text \n")


# rr = file_1.read()
# print(rr)
# print("#############")
# file_1.seek(0)
# for line in file_1:
#     print(line, end = "")
file_1.close()


