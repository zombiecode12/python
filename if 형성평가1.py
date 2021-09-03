"""
if-형성평가1.py

두개의 정수를 입력받아 큰수에서 작은수를 뺀 차를 출력하는
프로그램
"""
num1 = int(input("수를 입력해주세요"))
num2 = int(input("수를 입력해주세요"))

result = num1-num2 if num1 > num2 else num2-num1
print("결과:%d" %result)

if num1 > num2:
    result = num1 - num2
else :
    result = num2 - num1

print("결과2:%d" %result)
