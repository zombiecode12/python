print("계산기 입니다.")

while True:
    print("숫자를 입력하세요")
    a = int(input('수를 입력하세요'))
    b = int(input('수를 입력하세요'))
    print('a+b는 =%d입니다.'%(a+b))

    c = input('종료하시겠습니까? y/n:')
    if c == 'y' or c == 'Y':
        print('프로그램을 종료합니다.')
        break
