class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age



name = input('이름은? :')
age = input('나이는? :')
st = student(name, age)

print('학생의 이름은 %s입니다.' %st.name)
print('학생의 나이는 %s입니다.' %st.age)
