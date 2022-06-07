print("지금부터 타이머 시작을 누르고 문제를 풀어보세요.")
second = int(input("문제를 해결하셨나요? 총 몇 초가 걸렸나요?"))
# 65초 = 1분(60초) 5초   65/60 ==> 몫(분) 나머지(초)
# 123초 = 2분(120초) 3초  123/60 ==> 몫(분) 나머지(초)
# a 나누기 b = a/b
# 몫 : a//b
# 나머지 : a%b

minute = second // 60
remainder = second % 60

print(f"총 {minute}분 {remainder}초만에 문제를 해결하셨군요")