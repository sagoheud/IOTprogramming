# 파이썬 게임 프로그래밍

파이썬으로 게임을 만드는 방법을 학습합니다. tkinter와 pygame을 활용하여 고전 게임을 구현합니다.

## 📚 학습 목표

- tkinter를 이용한 벽돌깨기 게임 작성
- pygame을 이용한 외계 우주선 피하기 게임 작성

---

## 🎮 1. tkinter를 이용한 벽돌깨기 게임

### 주요 클래스 구조

#### Sprite 클래스 (기본 클래스)
```python
class Sprite():
    def __init__(self, canvas, item):
        self.canvas = canvas  # 캔버스 객체
        self.item = item      # 도형의 식별 번호
        self.speedx = 3       # x 방향 속도
        self.speedy = 3       # y 방향 속도
        self.x = 0            # 현재 x좌표
        self.y = 0            # 현재 y좌표
    
    def get_coords(self):
        return self.canvas.coords(self.item)
    
    def update(self):
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy
    
    def move(self):
        self.canvas.move(self.item, self.speedx, self.speedy)
    
    def delete(self):
        self.canvas.delete(self.item)
```

#### Ball 클래스
```python
class Ball(Sprite):
    def __init__(self, canvas, x, y, radius):
        self.radius = radius
        item = canvas.create_oval(x-self.radius, y-self.radius,
                                  x+self.radius, y+self.radius,
                                  fill='red')
        super().__init__(canvas, item)
    
    def update(self):
        x, y = self.get_position()
        width = self.canvas.winfo_width()
        # 벽에 부딪히면 방향 변경
        if x <= 0 or x >= width:
            self.speedx *= -1
        if y <= 0:
            self.speedy *= -1
```

#### Paddle 클래스
```python
class Paddle(Sprite):
    def __init__(self, canvas, x, y):
        self.width = 100
        self.height = 20
        item = canvas.create_rectangle(x - self.width / 2, y - self.height / 2,
                                       x + self.width / 2, y + self.height / 2,
                                       fill='white')
        super().__init__(canvas, item)
    
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        self.canvas.move(self.item, dx, dy)
```

#### Brick 클래스
```python
class Brick(Sprite):
    def __init__(self, canvas, x, y):
        self.width = 52
        self.height = 25
        item = canvas.create_rectangle(x - self.width / 2, y - self.height / 2,
                                       x + self.width / 2, y + self.height / 2,
                                       fill='yellow', tags='brick')
        super().__init__(canvas, item)
    
    def handle_collision(self):
        self.delete()
```

### 키보드 이벤트 처리
```python
# 캔버스가 키보드 이벤트를 받을 수 있도록 설정
self.canvas.focus_set()

# 화살표키와 스페이스키에 이벤트 연결
self.canvas.bind('<Left>', lambda _: self.paddle.move(-10, 0))
self.canvas.bind('<Right>', lambda _: self.paddle.move(10, 0))
self.canvas.bind('<space>', lambda _: self.start())
```

### 충돌 처리
```python
# 공과 다른 객체의 충돌 검사
coords = self.ball.get_coords()
items = self.canvas.find_overlapping(*coords)
objects = [self.shapes[x] for x in items if x in self.shapes]

# 충돌 처리
def collide(self, obj_list):
    if len(obj_list):
        self.speedy *= -1  # y 방향 변경
        for obj in obj_list:
            if isinstance(obj, Brick):
                obj.handle_collision()
```

---

## 🚀 2. pygame을 이용한 우주선 게임

### 설치
```bash
pip install pygame
```

### 기본 구조
```python
import pygame

pygame.init()
WIDTH = 600
HEIGHT = 400

# 화면 설정
mydisplay = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Shooting Game')

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 화면 업데이트
    mydisplay.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()
```

### 우주선 클래스
```python
class SpaceShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_bounding_rect()
        self.rect.x = 100
        self.rect.y = 100
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
```

### 적 우주선 클래스
```python
class EnemyShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('saucer.png')
        self.dx = -1
        self.rect = self.image.get_bounding_rect()
        self.rect.x = 500
        self.rect.y = 300
    
    def move(self):
        self.rect.x += self.dx
        if self.rect.x < 0:
            self.rect.x = 500
```

### 키보드 입력 처리
```python
key = pygame.key.get_pressed()
if key[pygame.K_UP]:
    y += -1
if key[pygame.K_DOWN]:
    y += 1
```

### 충돌 감지
```python
if pygame.sprite.spritecollideany(player, [enemy]):
    player.kill()
    running = False
```

---

## 🎯 게임 루프의 4가지 핵심 작업

1. **입력 처리**: 사용자의 키보드/마우스 입력 처리
2. **게임 업데이트**: 모든 게임 객체의 상태 업데이트 및 이동
3. **렌더링**: 화면 및 오디오 출력 업데이트
4. **속도 조절**: 게임 프레임 속도 제어

---

## 📝 두더지 게임 예제

간단한 두더지 게임 구현:
- 3x3 그리드에 버튼 배치
- 랜덤하게 두더지 표시
- 두더지를 클릭하면 점수 획득
- 빈 칸을 클릭하면 실패 카운트 증가

```python
def update():
    # 3초마다 랜덤하게 두더지 위치 변경
    x = randint(0, NUM_MOLES*NUM_MOLES-1)
    molesList[x]["image"] = mole_image
    window.after(3000, update)
```

---

## 🛠️ 기술 스택

- **tkinter**: Python 기본 GUI 라이브러리
- **pygame**: SDL 기반 게임 개발 라이브러리

## 📖 참고사항

- tkinter는 Python에 기본 포함
- pygame은 별도 설치 필요
- 충돌 검사는 사각형 영역(rect) 기반으로 수행
- 게임 루프에서 `after()` 또는 `pygame.display.update()` 사용

---

## 🎓 학습 포인트

1. **객체지향 프로그래밍**: 클래스를 활용한 게임 객체 구현
2. **상속**: Sprite 부모 클래스를 상속받아 Ball, Paddle, Brick 구현
3. **이벤트 처리**: 키보드 입력을 통한 게임 제어
4. **충돌 감지**: 게임 객체 간 충돌 검사 및 처리
5. **게임 루프**: 지속적인 화면 업데이트와 상태 관리
