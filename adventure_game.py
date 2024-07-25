import tkinter as tk
from character import Character
from events import events
import random
import logging

# 로그 설정 (콘솔 출력)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(message):
    logging.info(message)

def adventure_game(root):
    log_message("Program start")
    game_window = tk.Toplevel(root)
    game_window.title("Adventure Game")
    game_window.geometry("400x300")

    player = Character()  # 상태 초기화
    log_message("Initialize character state")

    def update_message(message):
        message_label.config(text=message)

    def show_status():
        log_message("show status")
        status_label.config(text=player.get_status())

    def next_event():
        log_message("next event")
        event = random.choice(events)
        update_message(event["question"])
        button1.config(text=list(event["choices"].keys())[0], command=lambda: choose_option(event, 0))
        button2.config(text=list(event["choices"].keys())[1], command=lambda: choose_option(event, 1))
        button1.grid(row=0, column=0, padx=10, pady=20)
        button2.grid(row=0, column=1, padx=10, pady=20)
        button1.config(state="normal")  # Re-enable button1
        button2.grid()  # Ensure button2 is visible and enabled

    def choose_option(event, choice_index):
        log_message("chosse option")
        choice_key = list(event["choices"].keys())[choice_index]
        outcome = event["choices"][choice_key]
        update_message(outcome)
        # "다음" 버튼 설정
        button1.config(text="다음", command=next_event)
        button1.grid(row=0, column=0, columnspan=2, pady=10)
        button2.grid_forget()  # Hide button2

    def start_game():
        log_message("start btn click")
        start_button.grid_forget()  # Hide start button
        next_event()  # Start the first event

    # 상태 버튼과 메시지 레이블을 포함하는 프레임 생성
    top_frame = tk.Frame(game_window)
    top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

    # 상태 확인 버튼
    status_button = tk.Button(top_frame, text="상태 보기", command=show_status)
    status_button.grid(row=0, column=0, pady=10, padx=10, sticky="w")

    # 상태 표시 레이블
    status_label = tk.Label(top_frame, text=player.get_status())
    status_label.grid(row=0, column=1, padx=10, sticky="w")

    # 초기 메시지
    message_label = tk.Label(game_window,
                             text="환영합니다! 모험 게임에 오신 것을 환영합니다."
                                  "\n당신은 어두운 숲에 있습니다. 앞으로 다양한 이벤트가 발생할 것입니다.",
                             wraplength=350)
    message_label.grid(row=2, column=0, columnspan=2, pady=20)

    # 선택지 버튼 프레임 생성
    button_frame = tk.Frame(game_window)
    button_frame.grid(row=3, column=0, columnspan=2, sticky="n")

    # 선택지 버튼
    button1 = tk.Button(button_frame, text="", width=15, height=2, command=lambda: None)
    button1.grid(row=0, column=0, padx=10, pady=20)

    button2 = tk.Button(button_frame, text="", width=15, height=2, command=lambda: None)
    button2.grid(row=0, column=1, padx=10, pady=20)

    # 시작 버튼 생성
    start_button = tk.Button(game_window, text="시작", command=start_game)
    start_button.grid(row=4, column=0, columnspan=2, pady=10)

    # 중앙 정렬을 위해 빈 열 추가
    game_window.grid_columnconfigure(0, weight=1)
    game_window.grid_columnconfigure(1, weight=1)

def on_closing(root):
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 메인 윈도우 숨기기
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    adventure_game(root)
    root.mainloop()

#test
