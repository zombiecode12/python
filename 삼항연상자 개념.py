"""
삼항연산자.py
삼항연산자를 이용하여 두 수중 작은 값 출력

"""
num1 = int(input("수를 입력해 주세요"))
num2 = int(input("수를 입력해 주세요"))

min_data = num2 if num1 > num2 else num1
print("min_data = %d" %min_data)
