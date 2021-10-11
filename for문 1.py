mark = [90,25,67,45,80]

number = 0

for marks in mark:
    number += 1
    if marks >= 60:
        print("%d번 학생은 합격입니다."%number)
    else:
        print("%d번 학생은 불합격"%number)
        
