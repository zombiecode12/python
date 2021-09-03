num1 = int(input("수를 입력해 주세요"))
num2 = int(input("수를 입력해 주세요"))
num3 = int(input("수를 입력해 주세요"))

if num1<num2 :
    min_data = num1
    if (min_data>num3):
       min_data = num3 
else:
    min_data = num2
    if min_data > num3 :
        min_data = num3
print("min_data = %d" %min_data)
    
