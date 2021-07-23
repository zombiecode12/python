"""
실수형 %f float
정수형 %d int
문자형 %s str
print - 출력: 문자열,변수,문자열+변수
input - 입력
기본으로 입력받았을 때 자료형은 문자형이다.
"""
name = input("이름을 입력해 주세요")
print(name)
print("안녕하세요 %s님" %name)
age = int(input("나이를 입력해주세요"))
height = float(input("키를 입력해주세요"))
print("나이: %d, 키:%.1fcm"%(age,height))
