n= int(input("введіть число:"))
num= 0
for item in range(1,n+1):
    if item % 2 == 0:
        num= num + item
print(num)