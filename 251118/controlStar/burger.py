print("="*20)
print("메뉴 1번 : 치즈버거")
print("메뉴 2번 : 치킨버거")
print("메뉴 3번 : 불고기버거")
print("="*20)
selection = int(input("메뉴를 선택하세요."))
#if selection >= 1 and selection <= 3: # 원래 맞는 표현
if 1 <= selection <=3: # 파이썬만 가능한 표현
    print(f"선택한 메뉴는 {selection} 입니다.")
else:
    print("잘못 입력했습니다.")