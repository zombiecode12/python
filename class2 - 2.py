class gamer:
    def __init__(self, NAME, LEVEL, SEVER):
       self.NAME = NAME
       self.LEVEL = LEVEL
       self.SEVER = SEVER

NAME = input('닉네임은? :')
LEVEL = int(input('레벨은? :'))
SEVER = input('서버는? :')

G = gamer(NAME, LEVEL, SEVER)

print('NAME : %s'%G.NAME)
print('LEVEL : %d'%G.LEVEL)
print('SEVER : %s'%G.SEVER)
