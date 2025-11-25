# Python GUI 프로그래밍 (Chapter 9)

## 📚 학습 목표
- tkinter를 이용한 간단한 GUI 프로그램 작성
- GUI의 일반적인 구조 이해
- 배치 관리자 사용법 숙지
- 위젯의 콜백 함수를 이용한 이벤트 처리
- 캔버스를 활용한 도형 그리기
- 애니메이션 구현

## 🎯 tkinter란?

**tkinter**는 파이썬에서 그래픽 사용자 인터페이스(GUI: Graphical User Interface)를 개발할 때 필요한 모듈입니다.

### 특징
- 유닉스 계열의 Tcl/Tk 위에 객체 지향 계층을 입힌 것
- John Ousterhout이 Tcl 스크립팅 언어를 위한 GUI 확장으로 개발
- 파이썬 표준 라이브러리에 포함

## 🪟 기본 윈도우 생성

### Hello tkinter 프로그램
```python
from tkinter import *  # tkinter 모듈 포함

window = Tk()  # 루트 윈도우 생성
label = Label(window, text="Hello tkinter")  # 레이블 위젯 생성
label.pack()  # 레이블을 윈도우에 배치
window.mainloop()  # 이벤트 처리 루프 시작
```

### 코드 분석
- `from tkinter import *`: tkinter 모듈 포함
- `window = Tk()`: 루트 윈도우 생성
- `label.pack()`: 압축 배치 관리자를 이용하여 위젯 배치
- `window.mainloop()`: 사용자 이벤트(마우스, 키보드)를 처리하는 루프

## 🧩 위젯(Widget) 종류

### 단순 위젯
- **Button**: 클릭 가능한 버튼
- **Canvas**: 도형을 그릴 수 있는 영역
- **Checkbutton**: 체크박스
- **Entry**: 텍스트 입력 필드
- **Label**: 텍스트나 이미지 표시
- **Message**: 여러 줄 메시지

### 컨테이너 위젯
- **Frame**: 다른 위젯을 담는 컨테이너
- **Toplevel**: 새 윈도우
- **LabelFrame**: 레이블이 있는 프레임
- **PanedWindow**: 크기 조절 가능한 패널

## 📐 주요 위젯 사용법

### 버튼 위젯
```python
button = Button(window, 
    text="클릭하세요!",
    bg="yellow",      # 배경색
    fg="blue",        # 전경색
    width=80, 
    height=2
)
button.pack()
```

### 엔트리 위젯
```python
entry = Entry(window, 
    fg="black", 
    bg="yellow", 
    width=80
)
entry.pack()
```

## 📦 배치 관리자 (Layout Managers)

### 1. 압축(Pack) 배치 관리자
위젯을 순서대로 배치

```python
Label(window, text="박스 #1", bg="red").pack()
Label(window, text="박스 #2", bg="green").pack()
Label(window, text="박스 #3", bg="blue").pack()
```

#### 옵션: side 파라미터
```python
Button(window, text="박스 #1").pack(side=LEFT)
Button(window, text="박스 #2").pack(side=LEFT)
Button(window, text="박스 #3").pack(side=LEFT)
```

### 2. 격자(Grid) 배치 관리자
테이블 형태로 배치

```python
b1 = Button(window, text="박스 #1")
b2 = Button(window, text="박스 #2")
b3 = Button(window, text="박스 #3")
b4 = Button(window, text="박스 #4")

b1.grid(row=0, column=0)  # 0행 0열
b2.grid(row=0, column=1)  # 0행 1열
b3.grid(row=1, column=0)  # 1행 0열
b4.grid(row=1, column=1)  # 1행 1열
```

#### Grid 옵션
- `columnspan`: 여러 열을 차지
- `rowspan`: 여러 행을 차지
- `sticky`: 정렬 방향 (N, S, E, W)

### 3. 절대(Place) 배치 관리자
픽셀 단위로 정확한 위치 지정

```python
b1 = Button(window, text="박스 #1")
b1.place(x=0, y=0)

b2 = Button(window, text="박스 #2")
b2.place(x=20, y=30)
```

### 윈도우 크기 설정
```python
window.geometry("600x100")  # Width x Height
```

## ⚡ 이벤트 처리

### 버튼 클릭 이벤트
```python
def process():
    print("버튼이 클릭되었습니다.")

button = Button(window, text="클릭하세요!", command=process)
button.pack()
```

### 카운터 예제
```python
counter = 0

def clicked():
    global counter
    counter += 1
    label['text'] = '버튼 클릭 횟수: ' + str(counter)

label = Label(window, text="아직 눌려지지 않음")
label.pack()

button = Button(window, text="증가", command=clicked)
button.pack()
```

### Entry 위젯 활용
```python
def process():
    tf = float(e1.get())  # 입력값 읽기
    tc = (tf - 32.0) * 5.0 / 9.0  # 화씨를 섭씨로 변환
    e2.delete(0, END)  # 기존 내용 삭제
    e2.insert(0, str(tc))  # 새 값 삽입

e1 = Entry(window)
e2 = Entry(window)
Button(window, text="화씨->섭씨", command=process).grid(row=2, column=1)
```

## 🎨 캔버스(Canvas) 그리기

### 기본 도형 그리기

#### 사각형
```python
canvas = Canvas(window, width=300, height=200)
canvas.pack()
canvas.create_rectangle(50, 25, 200, 100, fill="blue")
```

#### 원/타원
```python
canvas.create_oval(10, 10, 200, 150, fill="yellow")
```

#### 선
```python
canvas.create_line(10, 10, 200, 200, fill="green")
```

#### 다각형
```python
canvas.create_polygon(10, 10, 200, 50, 300, 160, fill="red")
```

#### 호(Arc)
```python
canvas.create_arc(10, 10, 200, 100, start=0, extent=120, fill="blue")
```

#### 텍스트
```python
canvas.create_text(200, 100, 
    fill="darkblue", 
    font="Times 30 italic bold",
    text="This is a text example."
)
```

### 도형 관리
```python
# 도형 생성
i = canvas.create_rectangle(50, 25, 200, 100, fill="red")

# 좌표 변경
canvas.coords(i, 0, 0, 100, 100)

# 색상 변경
canvas.itemconfig(i, fill="blue")

# 삭제
canvas.delete(i)
canvas.delete(ALL)  # 모든 항목 삭제
```

### 이미지 표시
```python
img = PhotoImage(file="image.png")
canvas.create_image(20, 20, anchor=NW, image=img)
```

### 색상 설정
```python
# 이름으로 지정
fill="red"

# RGB 16진수로 지정
fill="#FA88AB"
```

## 🖱️ 마우스와 키보드 이벤트

### 이벤트 바인딩
```python
def callback(event):
    print(event.x, event.y, "에서 마우스 이벤트 발생")

window.bind("<Button-1>", callback)
```

### 주요 이벤트 지정자
| 이벤트 | 설명 |
|--------|------|
| `<Button-1>` | 왼쪽 마우스 버튼 클릭 |
| `<Button-3>` | 오른쪽 마우스 버튼 클릭 |
| `<B1-Motion>` | 왼쪽 버튼 누른 채 이동 |
| `<ButtonRelease-1>` | 왼쪽 버튼 릴리즈 |
| `<Double-Button-1>` | 더블 클릭 |
| `<Enter>` | 마우스가 위젯 영역 진입 |
| `<Leave>` | 마우스가 위젯 영역 이탈 |
| `<Key>` | 키보드 입력 |
| `<Return>` | Enter 키 |

### 키보드 이벤트
```python
def key(event):
    print(repr(event.char), "가 눌렸습니다.")

frame.bind("<Key>", key)
```

## 🎬 애니메이션 구현

### 공 애니메이션
```python
from tkinter import *
import time
import random

window = Tk()
canvas = Canvas(window, width=600, height=400)
canvas.pack()

class Ball():
    def __init__(self, color, size):
        self.id = canvas.create_oval(0, 0, size, size, fill=color)
        self.dx = random.randint(1, 10)
        self.dy = random.randint(1, 10)
    
    def move(self):
        canvas.move(self.id, self.dx, self.dy)
        x0, y0, x1, y1 = canvas.coords(self.id)
        
        # 위아래 벽 충돌
        if y1 > canvas.winfo_height() or y0 < 0:
            self.dy = -self.dy
        
        # 좌우 벽 충돌
        if x1 > canvas.winfo_width() or x0 < 0:
            self.dx = -self.dx

# 공 생성
ball1 = Ball("blue", 60)
ball2 = Ball("green", 100)
ball3 = Ball("orange", 80)

# 애니메이션 루프
while True:
    ball1.move()
    ball2.move()
    ball3.move()
    window.update()
    time.sleep(0.05)

window.mainloop()
```

### 다중 공 애니메이션 (리스트 활용)
```python
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
ballList = []

# 30개의 공 생성
for i in range(30):
    ballList.append(Ball(random.choice(colors), 60))

# 애니메이션 루프
while True:
    for i in range(30):
        ballList[i].move()
    window.update()
    time.sleep(0.05)
```

## ✨ 핵심 정리

### tkinter 기본 구조
1. `from tkinter import *` - 모듈 import
2. `window = Tk()` - 루트 윈도우 생성
3. 위젯 생성 및 배치
4. `window.mainloop()` - 이벤트 루프 시작

### 배치 관리자 비교
| 관리자 | 사용 메소드 | 특징 |
|--------|------------|------|
| Pack | `.pack()` | 순서대로 배치, 간단 |
| Grid | `.grid()` | 테이블 형태, 정렬 용이 |
| Place | `.place()` | 절대 좌표, 정밀 제어 |

### 이벤트 처리 방법
- `command` 파라미터: 버튼 클릭 등 단순 이벤트
- `bind()` 메소드: 마우스, 키보드 등 복잡한 이벤트

---

## 📌 체크리스트
- [ ] tkinter로 기본 윈도우 생성
- [ ] 다양한 위젯 활용
- [ ] 배치 관리자로 레이아웃 구성
- [ ] 이벤트 처리 함수 작성
- [ ] 캔버스로 도형 그리기
- [ ] 마우스/키보드 이벤트 처리
- [ ] 간단한 애니메이션 구현

## 🎯 주요 메소드 참고

### Entry 위젯
- `get()`: 입력값 읽기
- `delete(start, end)`: 내용 삭제
- `insert(index, text)`: 텍스트 삽입

### Canvas 위젯
- `create_*()`: 도형 생성
- `coords()`: 좌표 변경
- `itemconfig()`: 속성 변경
- `move()`: 이동
- `delete()`: 삭제
