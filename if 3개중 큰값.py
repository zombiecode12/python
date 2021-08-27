num1 = int(input("수를 입력해주세요"))
num2 = int(input("수를 입력해주세요"))
num3 = int(input("수를 입력해주세요"))

if (num1 > num2):
    max_data = num1
else :
    max_data = num2
if max_data < num3:
   max_data = num3 

print("가장큰수 : %d" %max_data)
