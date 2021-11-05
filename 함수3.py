cur_temp = 33

def set_temp(temp):
    global cur_temp

    if (cur_temp < temp):
        while (cur_temp < temp):
            cur_temp += 1
            print("현제온도는 %d도 입니다." %cur_temp)
    else:
        while (cur_temp > temp):
            cur_temp -= 1
            print("현제온도는 %d도 입니다." %cur_temp)
print("띵띵")


while True:
    put_temp = input("원하는 온도를 입력해주세요 : ")

    if (put_temp=="종료"):
        print("에어컨을 종료합니다.")
        break
    elif (put_temp<="30" and put_temp >= "18"):
        print('현제 온도는 %d도 입니다.'%cur_temp)
        set_temp(int(put_temp))
    else:
        print('다시 입력하세요')
