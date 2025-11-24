# controlstmt.py
# 제어문 예제 모음 (간단한 활용 예)
# 실행하면 각 제어문의 동작을 콘솔에 출력합니다.

def if_examples(x):
    # 기본 if
    if x > 0:
        print("if: x는 양수입니다.")
    # if-else
    if x % 2 == 0:
        print("if-else: x는 짝수입니다.")
    else:
        print("if-else: x는 홀수입니다.")
    # if-elif-else
    if x == 0:
        print("if-elif-else: x는 0입니다.")
    elif x < 0:
        print("if-elif-else: x는 음수입니다.")
    else:
        print("if-elif-else: x는 양수입니다.")
    # 삼항 연산자
    sign = "양수" if x > 0 else ("0" if x == 0 else "음수")
    print("ternary:", sign)


def for_examples(items):
    # 기본 for
    print("for: items 출력")
    for it in items:
        print("-", it)
    # enumerate 사용
    print("for + enumerate:")
    for idx, val in enumerate(items, start=1):
        print(idx, val)
    # range 사용
    print("for + range:")
    for i in range(3):
        print("i =", i)
    # for-else: 루프가 정상 종료되었을 때 else 실행
    print("for-else 예제 (찾기):")
    target = 5
    for i in range(1, 6):
        if i == target:
            print("찾음:", i)
            break
    else:
        print("찾지 못함")


def while_examples(n):
    # 기본 while
    print("while: 1부터 n까지 합 계산")
    s = 0
    i = 1
    while i <= n:
        s += i
        i += 1
    print("sum =", s)
    # break와 continue
    print("while + break/continue 예제:")
    i = 0
    while i < 10:
        i += 1
        if i % 2 == 0:
            continue  # 짝수는 건너뜀
        if i > 7:
            print("8보다 크면 중단")
            break
        print("홀수:", i)
    else:
        print("while 정상 종료 (break 없이 끝난 경우 실행)")

def pass_example():
    # pass는 자리표시자
    for _ in range(2):
        pass
    print("pass 예제 완료 (아무 동작 없음)")

def main():
    print("== if_examples(3) ==")
    if_examples(3)
    print("\n== if_examples(0) ==")
    if_examples(0)

    print("\n== for_examples(['apple', 'banana', 'cherry']) ==")
    for_examples(['apple', 'banana', 'cherry'])

    print("\n== while_examples(5) ==")
    while_examples(5)

    print("\n== pass_example() ==")
    pass_example()

if __name__ == "__main__":
    main()