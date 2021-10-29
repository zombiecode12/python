def average(P_E, math, eng):
    hap = P_E + math + eng
    fin = hap/3
    return fin

P_E, math, eng = map(int, input("세 과목의 점수를 입력하세요 : ").split())
avg = average(P_E, math, eng)
print("평균 : %.2f"%avg)
