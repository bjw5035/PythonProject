lock = "비밀번호 입력하시오"
unlock = "Welcome!"
wrong_password = "잘못된 비밀번호 입니다."

password = "A1234!"
user_input = input("!!잠금!! 비밀번호를 입력하세요. \n")

# if 조건 :
#     실행문
# else :
#     실행문

if user_input == password :
    print("잠금이 해제되었습니다.")
    print(unlock)
else:
    print(wrong_password)