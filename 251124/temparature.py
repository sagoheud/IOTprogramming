#온도 입력 시 섭씨를 화씨로, 화씨를 섭씨로 출력하는 파이썬 예제

def c_to_f(c):
    """섭씨(C)를 화씨(F)로 변환"""
    return (c * 9/5) + 32

def f_to_c(f):
    """화씨(F)를 섭씨(C)로 변환"""
    return (f - 32) * 5/9

def temp_conv_case():
    """match/case를 사용한 온도 변환기"""
    print("--- 🌡️ Python 3.10+ 온도 변환기 (match/case) ---")
    
    # 1. 온도 값 입력
    try:
        t_input = float(input("변환할 온도를 입력하세요: "))
    except ValueError:
        print("오류: 유효한 숫자를 입력해야 합니다.")
        return

    # 2. 단위 입력 및 대문자 변환
    unit = input("현재 온도의 단위를 입력하세요 (C 또는 F): ").upper()

    # 3. match/case를 사용한 단위 처리
    match unit:
        case 'C':
            # 섭씨를 화씨로 변환
            c_temp = celsius_to_fahrenheit(temp_input)
            print(f"\n결과: 섭씨 {temp_input}°C는 화씨 {c_temp:.2f}°F 입니다.")
        case 'F':
            # 화씨를 섭씨로 변환
            c_temp = fahrenheit_to_celsius(t_input)
            print(f"\n결과: 화씨 {t_input}°F는 섭씨 {c_temp:.2f}°C 입니다.")
        case _: # default 케이스 (다른 모든 경우)
            print(f"오류: '{unit}'은 유효한 단위가 아닙니다. 'C' 또는 'F'를 입력하세요.")

if __name__ == "__main__":
    temp_conv_case()