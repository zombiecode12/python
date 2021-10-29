def my_mixer(fruit1,fruit2,fruit3):
    print("주스를 준비중입니다.")
    name1 = fruit1[0]
    name2 = fruit2[0]
    name3 = fruit3[0]
    juice = name1 + name2 + name3 + "주스"
    return juice

print(my_mixer("김치","김","조개"))
