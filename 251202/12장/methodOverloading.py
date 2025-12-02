class Test1:
    def abc(self):
        print("파라미터가 없는 함수")
    def abc(self,a):
        print(f"파라미터가 하나 {a}인 함수")
    def abc(self,a,b):
        print(f"파라미터가 {a}, {b}인 함수")
        
t1 = Test1()
# t1.abc()
# t1.abc("헬로 파이썬")
t1.abc(1,2)

# 파이썬은 오버로딩 기능을 지원하지 않는다
# 다른 언어는 지원한다