num_inp= int(input("введіть число:"))
list=[1,2,3,4,5,6,7,8,9,10]
for list_item in list:
    sum=list_item * num_inp
    print(num_inp,"*",list_item,"=",sum)