# 딕셔너리 : 예) dic_eng = {키1:값1, 키2:값2, ...}

dict_eng = {"apple" : "사과", "peach": "복숭아", "mango":"망고"}

user_input = input("검색할 영어 단어를 입력하세요 >>> ")

if user_input in dict_eng:
    print(f"검색하신 {user_input}의 뜻은 {dict_eng[user_input]}입니다.")
else:
    print("검색하신 단어는 등록되어 있지 않습니다.")
