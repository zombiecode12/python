"""
if-elif-else 개념
if 조건:
   실행문1
elif 조건 :
   실행문2
elif 조건:
   실행문3
else :
   실행문
elif = else if : 그렇지 않지만 만약 ~라면

프로그램 강제 종료 명령어 : exit()

if에 조건이 2개 이상일때
and: 교집합, 두조건 모두 참이어야 참일때
or: 합집합, 두조건중 하나만  참이어도 참일때

"""
score = int(input("점수를 입력해 주세요"))
if (score>100) or (score<0) :
    print("잘못 입력했습니다.")
    exit()
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else :
    print("F")
