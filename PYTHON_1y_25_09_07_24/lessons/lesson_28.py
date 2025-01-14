# my_file = open("test.txt", "w")
# my_file = open("test.txt", "a")
# my_file.write("\nand i am a teacher")

#
# my_file = open("test.txt", "r")
# for line in my_file:
#     print("Line from file: " + line)
# my_file.close()
#
# with open("test.txt", "r") as my_file:
#     for line in my_file:
#         print("Line from file: ", line)


import os

file_name = "output.txt"

os.system(f"ps aux | grep Spotify > {file_name}")

with open(file_name, "r") as my_file:
    for line in my_file:
        print("PS output: ", line)
