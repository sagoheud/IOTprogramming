# 파이썬 연산자 우선순위 예제 프로그램
# 파일: /c:/00python/basic/251124/operator.py
# 간단한 예제로 우선순위와 결합(associativity), 평가 순서(left-to-right) 등을 보여줍니다.

def side(name, val):
    # 호출 시 출력해서 평가 순서를 관찰
    print(f"evaluate {name!r}")
    return val

def examples():
    print("=== 산술 연산자 ===")
    print("2 + 3 * 4 =", 2 + 3 * 4)                # 3*4 먼저 -> 14
    print("(2 + 3) * 4 =", (2 + 3) * 4)          # 괄호로 우선순위 변경 -> 20

    print("\n=== 지수 연산자(우측 결합) ===")
    print("2 ** 3 ** 2 =", 2 ** 3 ** 2,
          "# 2 ** (3 ** 2) = 2 ** 9 = 512")

    print("\n=== 단항 연산자와 지수 ===")
    print("-3 ** 2 =", -3 ** 2, "# -(3 ** 2) = -9")
    print("(-3) ** 2 =", (-3) ** 2, "# (-3) ** 2 = 9")

    print("\n=== 비트 이동과 덧셈 ===")
    print("1 << 3 + 1 =", 1 << 3 + 1, "# 1 << (3 + 1) = 16")

    print("\n=== 비트 연산자 결합 ===")
    print("1 & 3 | 2 =", 1 & 3 | 2, "# (1 & 3) | 2 = 3")

    print("\n=== 비교 연산자 체이닝 ===")
    print("1 < 2 < 3 =", 1 < 2 < 3)

    print("\n=== 논리 연산자 우선순위 ===")
    print("False or True and False =", False or True and False,
          "# and 먼저 평가 -> False or (True and False) = False")

    print("\n=== 연산자 우선순위 vs 평가 순서 ===")
    # 곱셈은 덧셈보다 우선이지만, 피연산자의 평가는 왼쪽에서 오른쪽으로 이루어짐
    result = side('A', 1) + side('B', 2) * side('C', 3)
    print("result =", result)
    print("# 호출 순서: 'A' -> 'B' -> 'C' (피연산자평가는 좌측->우측), 계산은 B*C 후 A+(B*C)")

    print("\n=== walrus 연산자(대입식) 예 ===")
    if (n := 2 + 3 * 4):
        print("n := 2 + 3 * 4 ->", n, "# walrus로 대입(우선순위: 산술 내부 계산 후 대입)")

if __name__ == "__main__":
    examples()