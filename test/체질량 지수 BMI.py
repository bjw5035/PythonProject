height = float(input("키를 입력하세요(단위 : 미터) >>>"))
weight = float(input("몸무게를 입력하세요 >>>"))

# bmi = 몸무게 / 키 * 키
bmi = round(weight / height ** 2, 1)
bmi_icon = "ㅁ"

# 고도 비만 : 35 이상
# 중도 비만 (2단계 비만) : 30 ~ 34.9
# 경도 비만 (1단계 비만) : 25 ~ 29.9
# 정상 : 18.5 ~ 24.9 (25 미만)
# 저체중 : 18.5 미만

if bmi < 18.5 :
    print(bmi_icon)
    print("저체중입니다.")
elif bmi < 25 :
    print(bmi_icon * 2)
    print("정상입니다.")
elif bmi < 30 :
    print(bmi_icon * 3)
    print("경도 비만입니다.")
elif bmi < 35:
    print(bmi_icon * 4)
    print("중도 비만입니다.")
else:
    print(bmi_icon * 5)
    print("고도 비만입니다.")