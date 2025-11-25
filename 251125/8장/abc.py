'''
def abc():
    print("This is function abc")

def ghi():
    return "String"

abc()
print(ghi())
'''

class MyClass:
    def __init__(self, value):
        self.value = value

def abc(d):
    print(d)

a = "Hello world!"
abc(a)      #d = a

b =[1,2,3,4,5]
abc(b)      #d = b

c = MyClass(100)
abc(c)      #d = c의 객체주소