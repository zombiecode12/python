"""

if-형성평가2.py

정수를 입력받아 0이면 zero
양수이면 plus
음수이면 minus
"""
num = int(input("수를 입력해주세요"))

if num > 0:
    print("plus")
elif num==0:
    print("zero")
else :
    print("minus")
