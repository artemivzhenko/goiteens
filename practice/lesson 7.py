"""
user_value = int(input("please put your number\n"))
value = user_value ** 2 if user_value < 100 else user_value / 2
print(value)
x=input("please put x\n")
x=int(x)
y=input("please put y\n")
y=int(y)
message ="x bigger than y" if x>y else print("y bigger than x")
"""
"""
user_value=int(input("please put your number\n"))
value = user_value + 1 if user_value >=0 else user_value-2
print(value)
"""
"""
user_value =input("please put your number\n")
message ="число парное " if int(user_value)%2==0 else "число не парное "
value_len=len(user_value)
if value_len==1:
    message+="однозначное"
elif value_len==2:
    message+="двухзначное"
elif value_len==3:
    message+="трёхзначное"
print(message)
"""
