class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

a = Counter()
a.increment()
print(f"카운터의 값 = {a.count}") #출력: 카운터의 값 = 1
