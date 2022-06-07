rock = "가위"
scissor = "바위"
paper = "보"

import random as r

game_option = [rock, scissor, paper]
com_choice = r.randint(0, 2)

user_choise = int(input(" 0: 바위, 1: 가위, 2: 보 >>> "))

print("나의 선택 : ")
print(game_option[user_choise])

print("컴퓨터 선택 : ")
print(game_option[com_choice])

if com_choice == user_choise:
    print("비겼습니다.")
elif user_choise - com_choice == -1 or (user_choise == 2 and com_choice == 0):
    print("이겼습니다.")
else:
    print("졌습니다.")