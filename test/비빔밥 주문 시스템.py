menu = """
        - 메뉴 -
    불고기 비빔밥 : 12,000원
    야채 비빔밥 : 8,000원
    전주 비빔밥 : 10,000원
    
    세트 주문 시 : 3,000원 추가
    (세트는 밥과 반찬이 추가됩니다.)
"""

print("=" * 50)
print(menu)
print("=" * 50)
print()

order = input("비빔밥의 종류를 선택하세요. 예) 불고기, 야채, 전주 >>>")
combo = input("세트로 주문하시겠습니까? 3,000원 추가. 예) 네, 아니요 >>>>")

price = 0

if order == "불고기":
    price = 12_000
elif order == "야채":
    price = 8_000
else:
    price = 10_000

if combo == "네":
    # price = price + 3000
    price += 3000

print(f"총 금액은 {price}원 입니다.")
