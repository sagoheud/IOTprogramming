#include <iostream>
using namespace std;

int main() {
    int i, sevenSum = 0, otherSum = 0;

    // for(i = 1; i <= 100; i++){
    //     if (i%7 == 0)
    //         sevenSum += i;
    // }
    i = 1;
    while (i <= 100)
    {
        if (i%7 == 0)
            sevenSum += i;
        i++;
        continue;
    }
    
    cout << "1부터 100까지의 수 중 7의 배수들의 합 = " << sevenSum << "\n";

    // for(i = 1; i <= 100; i++){
    //     if (i%7 == 0)
    //         continue;
    //     otherSum += i;
    // }
    i = 1;                  //조건식
    while (i <= 100)        //조건식
    {
        if (i%7 == 0){
            i++;
            continue;       //while의 continue는 바로 조건식으로 감
        }
        otherSum += i;
        i++;                //증강식
    }

    cout << "1부터 100까지의 수 중 7의 배수 제외 합 = " << otherSum << "\n";
    cout << "두 합의 총 합 = " << sevenSum + otherSum << "\n";
    return 0;
}