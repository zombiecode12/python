"""
삼항연산자-활용.py
삼항연산자를 이용하여 세 수중 작은 값 출력

"""
num1 = int(input("수를 입력해 주세요"))
num2 = int(input("수를 입력해 주세요"))
num3 = int(input("수를 입력해 주세요"))

min_data = num1 if num1 < num2 else num2
min_data = num3 if min_data > num3 else min_data

print("min_data = %d " %min_data)

