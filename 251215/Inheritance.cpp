#include <iostream>
#include <string>
using namespace std;

class Vehicle { // Base class 부모클래스
    public:
        string brand = "Ford";
        void honk() {
            cout << "Tuut, tuut!\n"; 
        }
};

//Vehicle 클래스를 상속받아 Car 클래스 정의
class Car: publce Vehicle { // Derived class 자식클래스
    public:
        string model = "Mustang";
};

int main() {
    Car myCar; // Car 클래스의 객체 생성
    myCar.honk(); // Vehicle 클래스의 메서드 호출
    cout << myCar.brand + " " + myCar.model;
    return 0;
}