#include <iostream>
using namespace std;

//열거형 정의
enum Color{RED, GREEN, BLUE};
enum Weekday{MON = 1,    TUE,    WED,    THU,    FRI,    SAT,    SUN};

int main() {
    Color c = GREEN;  Weekday w = FRI;
    cout << "Color(GREEN)의 값: "  << c << endl;    //정수 1 출력
    cout << "Weekday(FRI)의 값: "  << w << endl;    //정수 5 출력

    //열거형으로 조건문 사용
    if (c == GREEN){
        cout << "현재 색상은 GREEN 입니다."  << c << endl;
    }
    //switch문 사용
    switch (w){
    case MON: cout << "월요일입니다."; break;
    case FRI: cout << "금요일입니다."; break;
    default: cout << "기타요일입니다."; break;
    }
    return 0;
}