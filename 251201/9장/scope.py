def varInc():
    global count                #local variable 지역변수
    count += 1
    print(f"Count = {count}")
    
count = 0                       #global variable 전역변수

print(count)
varInc()
print(count)