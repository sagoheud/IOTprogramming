#1~45의 숫자중 6개를 무작위로 추출, 보너스로 1개를 더 추출 후 
#순서대로 화면에 출력하는 복권 프로그램
import random
'''
class LottoGenerator:
    def __init__(self, start=1, end=45, count=6, bonus_count=1):
        # 로또 규칙을 인스턴스 변수로 저장 (기본값 1~45, 6개, 보너스 1개)
        self.start = start
        self.end = end
        self.count = count
        self.bonus_count = bonus_count
        self.all_numbers = list(range(self.start, self.end + 1))

    def generate(self):
        # 전체 숫자 범위에서 당첨 번호 6개 중복 없이 추출
        if len(self.all_numbers) < self.count + self.bonus_count:
            raise ValueError("번호 범위가 요구되는 번호 개수보다 적습니다.")
        
        # 1. 7개의 번호를 먼저 모두 추출 (당첨번호 + 보너스번호)
        total_selection = random.sample(self.all_numbers, self.count + self.bonus_count)
        
        # 2. 첫 6개는 당첨 번호로, 마지막 1개는 보너스 번호로 사용
        winning_numbers = total_selection[:self.count]
        bonus_number = [total_selection[self.count]]

        # 3. 당첨 번호를 오름차순으로 정렬
        winning_numbers.sort()
        
        return {
            "당첨 번호": winning_numbers,
            "보너스 번호": bonus_number
        }

lotto_maker = LottoGenerator()
result = lotto_maker.generate()

print("--- 클래스를 사용한 로또 번호 생성 결과 ---")
print(f"당첨 번호: {result['당첨 번호']}")
print(f"보너스 번호: {result['보너스 번호']}")
print("------------------------------------------")
'''

'''
# 클래스를 사용하지 않은 간단한 로또 번호 생성
all_numbers = list(range(1, 46))
selected_numbers = random.sample(all_numbers, 7)
winning_numbers = selected_numbers[:6]
bonus_number = [selected_numbers[6]]
winning_numbers.sort()
print("--------------- 로또 번호 당첨 결과 ---------------")
print(f"당첨 번호: {winning_numbers}")
print(f"보너스 번호: {bonus_number}")
print("--------------------------------------------------")
'''


#함수만 사용하여 로또 번호 생성하는 방법
def lotto():
    all_numbers = list(range(1, 46)) #1~45 숫자 리스트 생성
    selected_numbers = random.sample(all_numbers, 7) #7개 숫자 무작위 추출
    winning_numbers = selected_numbers[:6] #처음 6개는 당첨 번호
    winning_numbers.sort() #당첨 번호 오름차순 정렬
    bonus_number = [selected_numbers[6]] #마지막 1개는 보너스 번호

    return f"당첨 번호: {winning_numbers} \n보너스 번호: {bonus_number}"

print(lotto())