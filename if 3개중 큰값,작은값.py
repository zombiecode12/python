num1 = int(input("정수를 입력하세요"))
num2 = int(input("정수를 입력하세요"))
num3 = int(input("정수를 입력하세요"))

if num1 > num2 :
    max_data = num1
    min_data = num2 
else :
    max_data = num2
if max_data < num3:
    max_data = num3
else :
    if num3 < min_data :
        min_data = num3

print("가장큰수 : %d " %max_data)
print("가장작은수 : %d" %min_data)

    
