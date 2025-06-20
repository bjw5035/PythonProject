import tkinter as tk
from tkinter import messagebox
from pynput.mouse import Button, Controller
import threading
import time

# 마우스 컨트롤러
mouse = Controller()

# 매크로 실행 플래그
is_running = False

# 클릭 간 시간 기본값
click_interval = 0.2  # 기본 클릭 간격 (초)
pause_interval = 3.0  # 기본 대기 시간 (초)
click_count_threshold = 5  # 기본 클릭 횟수 (몇 번 후 대기)

# 클릭을 수행하는 함수
def start_clicking():
    global is_running
    click_count = 0

    while is_running:
        mouse.click(Button.left)
        click_count += 1
        print(f"클릭 {click_count}회 완료")

        time.sleep(click_interval)  # 클릭 간격 대기

        # 특정 횟수마다 일시 정지
        if click_count % click_count_threshold == 0:
            print(f"일시 정지: {pause_interval}초 대기")
            time.sleep(pause_interval)

# 매크로 시작
def start_macro():
    global is_running, click_interval, pause_interval, click_count_threshold

    if is_running:
        messagebox.showinfo("매크로 실행 중", "매크로가 이미 실행 중입니다.")
        return

    # 입력값 가져오기
    try:
        click_interval = float(entry_click_interval.get())
        pause_interval = float(entry_pause_interval.get())
        click_count_threshold = int(entry_click_count_threshold.get())
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 숫자를 입력해주세요.")
        return

    is_running = True
    thread = threading.Thread(target=start_clicking)
    thread.daemon = True
    thread.start()
    print("매크로 시작!")

# 매크로 중지
def stop_macro():
    global is_running
    if is_running:
        is_running = False
        print("매크로 중지!")
    else:
        messagebox.showinfo("매크로 중지", "매크로가 실행 중이 아닙니다.")

# UI 구성
root = tk.Tk()
root.title("마우스 매크로")

# 클릭 간격 입력
tk.Label(root, text="클릭 간격 (초):").grid(row=0, column=0, padx=10, pady=5)
entry_click_interval = tk.Entry(root)
entry_click_interval.insert(0, "0.2")
entry_click_interval.grid(row=0, column=1, padx=10, pady=5)

# 대기 시간 입력
tk.Label(root, text="대기 시간 (초):").grid(row=1, column=0, padx=10, pady=5)
entry_pause_interval = tk.Entry(root)
entry_pause_interval.insert(0, "3.0")
entry_pause_interval.grid(row=1, column=1, padx=10, pady=5)

# 클릭 횟수 기준 입력
tk.Label(root, text="대기 전 클릭 횟수:").grid(row=2, column=0, padx=10, pady=5)
entry_click_count_threshold = tk.Entry(root)
entry_click_count_threshold.insert(0, "5")
entry_click_count_threshold.grid(row=2, column=1, padx=10, pady=5)

# 버튼
btn_start = tk.Button(root, text="매크로 시작", command=start_macro, bg="green", fg="white")
btn_start.grid(row=3, column=0, padx=10, pady=10)

btn_stop = tk.Button(root, text="매크로 중지", command=stop_macro, bg="red", fg="white")
btn_stop.grid(row=3, column=1, padx=10, pady=10)

# 메인 루프 실행
root.mainloop()
