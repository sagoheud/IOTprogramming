#include <iostream>
#include <string>
using namespace std;

// 구조체 정의
struct Person {
    string name;
    int age;
    double height;
};

int main() {
    // 구조체 변수 선언 및 초기화
    Person person1;
    person1.name = "Alice";
    person1.age = 25;
    person1.height = 165.5;

    // 구조체 값 출력
    cout << "Name: " << person1.name << endl;
    cout << "Age: " << person1.age << endl;
    cout << "Height: " << person1.height << " cm" << endl;

    // 구조체 배열 사용 예시
    Person people[2] = { {"Bob", 30, 175.0}, {"Charlie", 22, 180.2} };

    for (int i = 0; i < 2; i++) {
        cout << "Person " << i+1 << ": " 
             << people[i].name << ", "
             << people[i].age << " years, "
             << people[i].height << " cm" << endl;
    }

    return 0;
}
