# append function in file 
# to close the file automatically use with class

with open("sample.txt", "a") as file:
    file.write("\nThis line is appended to this file.")
    