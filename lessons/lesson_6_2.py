record= input("введіть:")
print(record)
record_list= record.split(",")
num= int(record_list[0])
sym= record_list[1]

sum= num * sym
print(sum)