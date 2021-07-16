"""
변수는: 데이터가 저장 되는 공간
컴퓨터에서는 메모리가 존재한다.
데이터 타입: 문자열,숫자
정수형(소숫점x), 실수형(소숫점ㅇ)
변수를 만든다 = 변수를 선언한다.
"""

#문자열 (string) %s
name = "승호"
#정수형 (int) %d
grade = 6
#실수형(float)%f
height = 166.45555555

#문자열 출력
print("안녕하세요")
#변수 출력
print(name)
#문자열 + 변수 출력 : 데이터 포매팅(format)
print("이름:%s" %name)
print("학년:%d" %grade)
print("키:%.1f" %height)
