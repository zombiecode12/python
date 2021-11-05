import random
print('영어단어찾기 게임')


words = ['cat', 'dog', 'cow', 'pan', 'fan']
word = random.choice(words)

guesses = []

for _ in range(10):
    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print('_', end= ' ')
    print()

    guess = input('알파벳을 입력하시오')
    guesses.append(guess)

    found_all = True
    for char in word:
        if char not in guesses:
            found_all = False
    if found_all:
        print('승리')
        break
