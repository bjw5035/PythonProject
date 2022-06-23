import pyautogui
import time

# 1. 화면 크기 출력
print(pyautogui.size())

# 2. 마우스 위치 출력
time.sleep(2)
print(pyautogui.position())

# 3. 마우스 이동
# pyautogui.move(41, 442)
pyautogui.moveTo(41, 442, 2)

# 4. 마우스 클릭
pyautogui.click()
pyautogui.click(button='right')
pyautogui.doubleClick()
pyautogui.click(click=3, interval=1) # 3번 클릭할건데 1초마다 해라

# 5. 마우스 드래그
# 1792,416 -> 1611,128
pyautogui.moveTo(1792,416, 2)
pyautogui.dragTo(1611,128, 2)