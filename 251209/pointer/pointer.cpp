#include <iostream>
using namespace std;

int main()
{
    string food = "Pizza";  // int *p
    string *ptr = &food;  // 선언문에서 *는 포인터 변수를 만들기 위한 기호
    // A pointer variable, with the name ptr, that stores the address of food
    // 일반 변수는 주소를 담을 수 없다. 포인터 변수는 주소를 담는 변수

    cout << food << "\n";   // Output (Pizza)
    cout << &food << "\n";  // Output  (0x5ffe00)
    cout << ptr << "\n";    // Output  (0x5ffe00)
    cout << *ptr << "\n";   // 실행문에서 *는 간접참조 (역참조)를 가르킴
    // Output (Pizza)

    return 0;
}