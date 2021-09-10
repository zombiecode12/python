"""
1~12 사이의 정수를 입력받아 입력받은 월의 날수를
출력하는 프로그램
"""

month = int(input("월을 입력하시오"))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("%d월은 31일 입니다." %month)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("%d월은 30일 입니다." %month)
elif month == 2:
    print("2월은 28일 입니다.")
else :
    print("존재하지 않는 달 입니다.")
