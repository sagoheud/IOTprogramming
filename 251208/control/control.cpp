#include <iostream>
using namespace std;

int main() {
   int score;

   printf("Input score: ");
   scanf("%d", &score);
   
//    if(score >= 90)
//     printf("A 등급\n");
//    else if(score >= 80)
//     printf("B 등급\n");
//    else if(score >= 70)
//     printf("C 등급\n");
//    else if(score >= 60)
//     printf("D 등급\n");
//    else
//     printf("F 등급\n");

    switch (score/10) //파이썬의 match case의 경우 한 블록 실행시 구문 벗어나지만
    //여기선 break문이 없을 경우 해당하는 값들 모두 실행 된다.
    {
    case 10:
    case 9:
        printf("A 등급\n"); break;
    case 8:
        printf("B 등급\n"); break;
    case 7:
        printf("C 등급\n"); break;
    case 6:
        printf("D 등급\n"); break;
    default:
        printf("F 등급\n");
    }
    
   return 0;
}