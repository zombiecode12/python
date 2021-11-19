class score:
    def __init__(self, name, kor, eng):
        self.name = name 
        self.kor = kor
        self.eng = eng

    def prn(self):
        print('%s %d %d'%(self.name, self.kor, self.eng))



name, kor, eng = input('이름, 국어점수, 영어점수: ').split()
st1 = score(name, int(kor), int(eng))

name, kor, eng = input('이름, 국어점수, 영어점수: ').split()
st2 = score(name, int(kor), int(eng))

hap = score('합계', st1.kor + st2.kor, st1.eng + st2.eng)

st1.prn()
st2.prn()
hap.prn()
