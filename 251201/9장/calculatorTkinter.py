from tkinter import *
from tkinter import font

window = Tk()
window.title("My Calculator")

# 1. 디스플레이 위젯 생성
display = Entry(window, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5, sticky="nsew") # sticky 추가

# 폰트 위젯 생성
display_font = font.Font(family="Arial")
display.config(font=display_font)

# 폰트 사이즈 변경
def resize_font(event):
    new_size = max(int(event.width / 30), 10)
    display_font.configure(size=new_size)
    button_font.configure(size=max(int(new_size / 1.5), 8))
    

# 2. 클릭 함수 정의 (가장 중요)
def click(key):
    if key == 'C':
        display.delete(0, END)
    elif key == '=':
        try:
            # eval() 함수로 수식 계산
            result = eval(display.get())
            display.delete(0, END)
            display.insert(END, str(result))
        except:
            # 계산 오류 처리
            display.delete(0, END)
            display.insert(END, "오류")
    else:
        display.insert(END, key)

# 3. 버튼 리스트 및 배치
button_list = [
'7', '8', '9', '/', 'C',
'4', '5', '6', '*', ' ',
'1', '2', '3', '-', ' ',
'0', '.', '=', '+', ' ' ]

row_index = 1
col_index = 0

button_font = font.Font(family="Arial")

for button_text in button_list:
    # 4. 버튼 생성 시 command 옵션에 click 함수 연결
    # lambda 함수를 사용하여 button_text를 click 함수의 인수로 전달
    if button_text != ' ': # 공백 버튼은 생성하지 않음
        Button(window, text=button_text, font=button_font,\
                command=lambda b=button_text: click(b))\
                .grid(row=row_index, column=col_index,\
                sticky="nsew", padx=1, pady=1)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
        
# 모든 버튼의 크기와 글자 크기가 1행부터 5행까지 
# 동일한 비율(1)로 확장되도록 설정
for i in range(5): 
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)    
    window.bind('<Configure>', resize_font)
        
window.mainloop()