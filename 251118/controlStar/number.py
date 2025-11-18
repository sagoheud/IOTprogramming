'''
hap = 0
number = int(input("정수 입력 : "))

for i in range(number + 1):
    hap += i
print(f"1부터 {number}까지의 합은 {hap} 입니다.")
'''

totalSum = 0
evenSum = 0
oddSum = 0
sevenSum = 0

for i in range(101):
    totalSum += i
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
    if i % 7 == 0:
        sevenSum += i

print(f"1부터 100 까지의 홀수들의 합은 {oddSum} 입니다.")
print(f"1부터 100 까지의 짝수들의 합은 {evenSum} 입니다.")
print(f"1부터 100 까지의 7의 배수들의 합은 {sevenSum} 입니다.")
print(f"1부터 100 까지의 전체 합은 {totalSum} 입니다.")