"""
if-elif-else 활용.py
복식 체급 출력 프로그램
몸무게를 입력받아 그에 맞는 복싱 체급을 출력하는 프로그램
50.80 kg 이하는 Flyweight
61.23 kg 이하는 Lightweight
72.57 kg 이하는 Middleweight
88.45 kg 이하는 Cruiserweight
그이상은 Heavyweight

"""
weight = float(input("몸무게를 입력해 주세요"))

if (weight <= 0) or (weight > 200) :
    print("잘못 입력하셨습니다.")
    exit()
     
if weight <= 50.80 :
    print("Flyweight")
elif weight <= 61.23 :
    print("Lightweight")
elif weight <= 72.57 :
    print("Middleweight")
elif weight <= 88.45 :
    print("Cruiserweight")
else :
    print("Heavyweight")
   
