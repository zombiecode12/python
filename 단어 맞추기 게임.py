print("="*50)
print("영어단어 맞추기 게임")
print("="*50)

dic = {
    "lion":"사자",
    "nuclear":"원자핵의",
    "elect":"선출하다",
    "valuable":"가치있는",
    "sun":"태양"}
for word in dic.keys():
    korean = dic[word]
    guess = input("{}단어를 번역하세요".format(word))

    if guess == korean:
        print("정답")
    else:
        print("오답")

print("프로그램 종료")
