import pygame
import sys

# 1. 게임 기본 설정
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("파이썬 벽돌깨기")

# 폰트 설정
font = pygame.font.Font(None, 36)

# 2. 게임 객체 클래스 정의

# 2-1. 패들 클래스 (수정 없음)
class Paddle(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color
        self.speed = 8

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self)

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        
        # 화면 경계 충돌 처리
        if self.left < 0:
            self.left = 0
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

# 2-2. 공 클래스
class Ball(pygame.Rect):
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, size)
        self.color = color
        self.speed_x = 4  # 초기 속도
        self.speed_y = -4 # 위로 움직이도록 설정
        self.ball_size = size # ✨ 변수 이름 변경

    def draw(self, surface):
        # self.ball_size를 사용하여 원 그리기
        pygame.draw.circle(surface, self.color, self.center, self.ball_size // 2)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # 화면 벽 충돌 처리 (상, 좌, 우)
        if self.top <= 0:
            self.speed_y *= -1 # 상단 벽
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.speed_x *= -1 # 좌우 벽

# 2-3. 벽돌 클래스 (수정 없음)
class Brick(pygame.Rect):
    def __init__(self, x, y, width, height, color, points):
        super().__init__(x, y, width, height)
        self.color = color
        self.points = points # 벽돌 점수
        self.is_broken = False

    def draw(self, surface):
        if not self.is_broken:
            pygame.draw.rect(surface, self.color, self)
            pygame.draw.rect(surface, BLACK, self, 1) # 테두리

# 3. 객체 초기화 및 게임 상태 설정

# 패들 객체
paddle_width = 100
paddle_height = 15
paddle = Paddle(
    (SCREEN_WIDTH - paddle_width) // 2, 
    SCREEN_HEIGHT - 30, 
    paddle_width, 
    paddle_height, 
    BLUE
)

# 공 객체
ball_size = 12
# 이 부분에서 ball_size(12)가 Ball.__init__의 size로 전달됩니다.
ball = Ball(
    SCREEN_WIDTH // 2, 
    SCREEN_HEIGHT - 50, 
    ball_size, 
    WHITE
)

# 벽돌 생성 (생략)
brick_rows = 5
brick_cols = 10
brick_width = 70
brick_height = 20
brick_padding = 5
brick_offset_x = (SCREEN_WIDTH - (brick_cols * (brick_width + brick_padding))) // 2
brick_offset_y = 50

bricks = []
brick_colors = [RED, YELLOW, GREEN, BLUE, RED]
for row in range(brick_rows):
    color = brick_colors[row % len(brick_colors)]
    points = (brick_rows - row) * 10
    for col in range(brick_cols):
        brick_x = brick_offset_x + col * (brick_width + brick_padding)
        brick_y = brick_offset_y + row * (brick_height + brick_padding)
        bricks.append(Brick(brick_x, brick_y, brick_width, brick_height, color, points))

# 게임 상태 변수 (생략)
score = 0
game_over = False
running = True
clock = pygame.time.Clock()

# 4. 게임 루프 (생략)
while running:
    # 4-1. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            score = 0
            game_over = False
            # 재시작 시 공 객체도 수정된 Ball 클래스로 재생성
            ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50, ball_size, WHITE)
            bricks = []
            for row in range(brick_rows):
                color = brick_colors[row % len(brick_colors)]
                points = (brick_rows - row) * 10 
                for col in range(brick_cols):
                    brick_x = brick_offset_x + col * (brick_width + brick_padding)
                    brick_y = brick_offset_y + row * (brick_height + brick_padding)
                    bricks.append(Brick(brick_x, brick_y, brick_width, brick_height, color, points))

    # 패들 이동 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move("left")
    if keys[pygame.K_RIGHT]:
        paddle.move("right")

    # 4-2. 게임 로직 업데이트
    if not game_over:
        ball.move()

        # 공과 패들 충돌 처리
        if ball.colliderect(paddle):
            ball.speed_y *= -1
            relative_intersect_x = (paddle.centerx - ball.centerx)
            paddle_width = 100 # 패들 너비 정의가 위쪽에 없으므로 다시 정의
            ball.speed_x = -relative_intersect_x / (paddle_width / 2) * 4

        # 공과 벽돌 충돌 처리
        for brick in bricks[:]:
            if not brick.is_broken and ball.colliderect(brick):
                brick.is_broken = True
                score += brick.points
                ball.speed_y *= -1
                
                if all(b.is_broken for b in bricks):
                    game_over = True
                    game_over_text = "🎉 WIN! Score: {} 🎉".format(score)
                    break
        
        # 게임 오버 조건
        if ball.bottom >= SCREEN_HEIGHT:
            game_over = True
            game_over_text = "Game Over! Score: {}".format(score)

    # 4-3. 화면 그리기 (Drawing)
    screen.fill(BLACK)

    if not game_over:
        paddle.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)
        
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    else:
        text_surface = font.render(game_over_text, True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)

        restart_text = font.render("Press SPACE to Restart", True, YELLOW)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(restart_text, restart_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()