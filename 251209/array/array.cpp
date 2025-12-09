#include <iostream>
#define STD_NUM 5
using namespace std;

int main() {
    int intArr[STD_NUM], i, sum = 0;
    int leng = sizeof(intArr)/sizeof(int);
    //정수는 4바이트 의 데이터 공간을 차지하고, 
    //배열은 배열의 사이즈와 정수 리터럴값의 곱의 크기만큼 데이터 공간 차지함

    for (i = 0; i < leng; i++)
    {
        cin >> intArr[i];
    }
    

    for (i = 0; i < leng; i++)
    {
        cout << intArr[i] << " ";
    }

    for (i = 0; i < leng; i++){
        sum += intArr[i];
    }

    cout << "합 = " << sum << ", ";
    cout << "평균 = " << (double)sum/leng << "\n";

    return 0;
}