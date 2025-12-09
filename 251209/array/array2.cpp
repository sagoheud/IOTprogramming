#include <iostream>
#include <cstdlib>      //메모리 관리, 프로세스 제어, 형 변환, 의사 난수 생성
#include <ctime>        //시스템 시간 및 날짜 , 시간 간격 측정, 시간을 문자열로 변환
// 난수는 시드를 기준으로 생성하는데 시드는 컴퓨터 시스템 시관과 관련되어 있음
using namespace std;


int main() {
    const int num = 5;
    int intArr[num] = {0}, i, oddSum = 0, evenSum = 0;
    int leng = sizeof(intArr)/sizeof(int);
    srand(time(NULL));      //기본 시드는 1로 고정되어 있으므로 이부분에서 랜덤 시드 부여

    for (i = 0; i < leng; i++)
        cout << intArr[i] << " ";   //초기값 0인 배열 출력

    for (i = 0; i < leng; i++)
        intArr[i] = rand() % 100;   //랜덤 인수 삽입
    for (i = 0; i < leng; i++)
        cout << intArr[i] << " ";   //랜덤 인수 삽입된 배열 출력
    
    for (i = 0; i < leng; i++)
    {
        if ((i+1) % 2 == 1)
            oddSum += intArr[i];    //홀수 항 총합
        else
            evenSum += intArr[i];   //짝수 항 총합
    }

    cout << "\n홀수항의 합 = " << oddSum;
    cout << "\n짝수항의 합 = " << evenSum;
    return 0;
}