import random
import time

words = ["가","나","다","라","마","바","사","아","자","차"]

n = 1

print("준비되면 엔터")
input()
start = time.time()
q = random.choice(words)

while n <=5:
    print("*문제:",n)
    print(q)
    x=input()
    if q==x:
        print("통과")
        n +=1
        q=random.choice(words)
    
    else:
        print("오타입니다.")

end = time.time()
et = end-start
et = format(et, ".2f")
print("총 걸린 시간 : ", et, "초")
