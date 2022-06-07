# 원의 넓이 : 반지름 * 반지름 * 3.14
# 원의 둘레 : 2 * 반지름 * 3.14

# int : 정수
# float : 실수
# 거듭제곱 : **
# 반올림 : round, 소숫점 : (자릿수) 에:) round(area, 자릿수)
r = float(input("반지름을 입력해 주세요. \n"))
area = r ** 2 * 3.14
circumference = 2 * r * 3.14
print(f"원의 넓이(거듭제곱) : {round(area, 2)}")
print(f"원의 둘레 : {round(circumference)}")
