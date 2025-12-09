#include <iostream>
using namespace std;

int main() {
    string food = "Pizza";
    string &meal = food;    // 얕은 복사 (기존값 바뀜, 주소값 공유)
    string water = food;    // 깊은 복사 (새로운 주소값으로 생성)

    meal[0] = 'B';
    water[0] = 'D';
    cout << food << "\n";  // Outputs Bizza
    cout << meal << "\n";  // Outputs Bizza
    cout << water << "\n"; // Outputs Dizza
    cout << &food;         // 메모리 주소 연산 (&주소 연산자)
    return 0;
}