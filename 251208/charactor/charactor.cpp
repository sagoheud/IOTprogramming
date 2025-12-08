#include <iostream>
using namespace std;

int main() {
    char a = 65, b = 66, c = 67;
    printf("%c, %c, %c\n", a, b, c);

    char ch = 'A';              //해당 문자의 ASCII 코드 값이 할당됨
    printf("ch = %c\n", ch);
    ch = 0x41;
    printf("ch = %c\n", ch);
    ch = 65;
    printf("ch = %c\n", ch);
    return 0;
}