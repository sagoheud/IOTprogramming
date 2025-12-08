#include <iostream>
using namespace std;

int main() {
   int i = 0, sum = 0;

   for (i; i <= 100; i++){      //for(초기식; 조건식; 증강식) --> 조건에 되야 실행
      sum += i;
   }
   printf("1부터 100까지의 합 = %d\n", sum);

   i = 0, sum = 0;                           //while(초기식) --> 조건에 되야 실행
   while (i <= 100){                         //(조건식);
      sum += i;                              
      ++i;                                   //(증강식);
   }
   printf("1부터 100까지의 합 = %d\n", sum);

   i = 0, sum = 0;                           //초기식;
   do {                                      //do --> 무조건 한번 실행
      sum += i;                              
      ++i;                                   //증강식;
   } while (i <= 100);                       //조건식;
   printf("1부터 100까지의 합 = %d\n", sum);
   


   return 0;
}