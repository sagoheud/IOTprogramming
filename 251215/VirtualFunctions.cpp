#include <iostream>
using namespace std;

class Animal {
  public:
    virtual void sound() {
      // Animal::sound(); // 사용시 출력으로 기본 클래스의 함수 호출
      cout << "Animal sound\n";
    }
};

class Dog : public Animal {
  public:
    void sound() override {
      cout << "Dog barks\n";
    }
};

class Cat : public Animal {
  public:
    void sound() override {
      cout << "Cat miao\n";
    }
};

int main() {
  Animal* a;
  Dog d; Cat c;
  a = &d; a->sound(); // Outputs: Dog barks
  a = &c; a->sound(); // Outputs: Cat miao
  return 0;
}