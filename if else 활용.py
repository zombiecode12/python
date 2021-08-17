"""
if-else 활용.py
나이를 입력받아 20살 이상이면 "An adult" 라고 출력
그렇지 앟으면 몇년수에 성인이 되는지 "숫자 years"
라고 출력하는 프로그램
"""
age = int(input("나이를 입력해 주세요"))

if age >= 20:
    print("An adult")
else :
    print("%d years" %(20-age))
    
