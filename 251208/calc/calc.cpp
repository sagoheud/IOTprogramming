#include <iostream>
using namespace std;

int main() {
    int x, y;
    cout << "첫 번째 정수 입력: ";
    cin >> x;
    cout << "두 번째 정수 입력: ";
    cin >> y;
    cout << x << "+" << y << "=" << (x + y) << "\n";
    cout << x << "-" << y << "=" << (x - y) << "\n";
    cout << x << "*" << y << "=" << (x * y) << "\n"; 
    cout << x << "/" << y << "=" << ((float)x / y) << "\n";
    cout << "정수와 정수를 연산하면 컴파일러형 언어는 결과가 무조건 정수임\n";
}