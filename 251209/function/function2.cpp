#include <iostream>
using namespace std;
void swap1(int a, int b){   // 값만 전달
    int temp;
    temp = a;
    a = b;
    b = temp;
}
void swap2(int &a, int &b){ // 주소를 전달
    int temp;
    temp = a;
    a = b;
    b = temp;
}

int main(){
    int x = 1, y = 2;
    swap1(x, y);
    cout << "x = " << x << ", y = " << y << endl;
    swap2(x, y); // &로 인해 x,y 값도 바뀜
    cout << "x = " << x << ", y = " << y << endl;

    return 0;
}