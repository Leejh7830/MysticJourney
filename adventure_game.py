import tkinter as tk
from tkinter import messagebox
from character import Character

def adventure_game():
    game_window = tk.Toplevel()
    game_window.title("Adventure Game")
    game_window.geometry("400x300")


    player = Character() # 주인공 상태 초기화

    def update_message(message):
        message_label.config(text=message)

    def update_status():
        status_label.config(text=player.get_status())

    def show_status():
        update_status()

    # 상태 버튼과 메시지 레이블을 포함하는 프레임 생성
    top_frame = tk.Frame(game_window)
    top_frame.pack(side="top", fill="x")

    # 상태 확인 버튼
    status_button = tk.Button(top_frame, text="상태 보기", command=show_status)
    status_button.pack(side="left", pady=10, padx=10)

    # 상태 표시 레이블
    status_label = tk.Label(top_frame, text=player.get_status())
    status_label.pack(side="left", padx=5)

    # 초기 메시지
    message_label = tk.Label(game_window,
                             text="환영합니다! 모험 게임에 오신 것을 환영합니다."
                                  "\n당신은 어두운 숲에 있습니다. 앞으로 두 갈래 길이 있습니다."
                                  "\n왼쪽 길로 가면 어쩌면 안전할 수도 있고, 오른쪽 길로 가면 위험할지도 모릅니다.",
                             wraplength=350)
    message_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 메인 윈도우 숨기기
    adventure_game()
    root.mainloop()