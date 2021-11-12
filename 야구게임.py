import random

print('숫자 야구 게임')
print('생각한 숫자를 맞추는 게임입니다.')

numbers = []
for _ in range(3):
    while True:
        if len(numbers) == 0:
            number = random.randint(1,9)
        else:
            number = random.randint(0,9)

        if number not in numbers:
            numbers.append(number)
            break

for _ in range(10):
    guesses = input('생각한 숫자를 맞추세요(중복되지않는 세가지 수)')
    guesses = list(guesses)

    strike = 0
    ball = 0
    out = 0

    for i in range(3):
        if int(guesses[i]) == numbers[i]:
            strike += 1
        elif int(guesses[i]) in numbers:
            ball += 1
        else:
            out += 1

    print(strike,'스트라이크', ball, '볼', out,'아웃')

    if strike == 3:
        break
