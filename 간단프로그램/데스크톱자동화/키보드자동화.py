import pyautogui
import pyperclip

# 2. 키보드 입력 (키)
# pyautogui.press('enter')
# pyautogui.press('up')

# 3. 키보드 입력 (여러개 동시에)
# pyautogui.hotkey('ctrl', 'c') # mac = command

# 4. 한글 입력 방법
pyperclip.copy('한글입력 잘되나?')
pyperclip.hotkey('ctrl', 'v')