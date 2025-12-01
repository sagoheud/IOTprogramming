from tkinter import Tk, Label

def create_label(parent, text, font_size=12):
    """레이블을 생성하는 함수"""
    label = Label(parent, text=text, font=("Arial", font_size))
    label.pack(padx= 50, pady=50)
    return label

def main():
    # 윈도우 생성
    window = Tk()
    window.title("간단한 윈도우")
    window.geometry("400x300")
    
    # 함수로 레이블 생성
    create_label(window, "안녕하세요!", font_size=14)
    create_label(window, "이것은 레이블입니다.", font_size=10)
    
    # 윈도우 실행
    window.mainloop()

if __name__ == "__main__":
    main()