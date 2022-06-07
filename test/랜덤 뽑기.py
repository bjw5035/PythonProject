import random as r
import time as t

print("!! 커피 값 내기 !! 오늘은 누가 커피를 사게 될까요? ")
name = input("참가자들의 이름을 입력해 주세요. 예) 철수 영희 >>> ").split()

print(f"총 {len(name)}명 참가하셨습니다.")

winner = r.choice(name)

print("오늘 선택된 사람은 ...")
t.sleep(5) # 초

print(f"{winner}님 입니다.")