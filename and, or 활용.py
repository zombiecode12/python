num1 = int(input("주사위를 굴려주세요"))
num2 = int(input("주사위를 또한번 굴려주세요"))
if (num1 > 6) or (num2 > 6) or (num1 <= 0) or (num2 <= 0):
    print("잘못입력했습니다.")
    exit()
if (num1 >= 4) and (num2 >= 4):
    print("이겼습니다.")
elif (num1 >= 4) or (num2 >= 4): 
    print("비겼습니다.")
else :
    print("졌습니다.")

 
