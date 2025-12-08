#include <iostream>
using namespace std;

int main() {
   int a = 3, b = 7;    //0000 0011
                        //0000 0111
   printf("%d & %d = %d\n", a, b, (a & b));
   printf("%d && %d = %d\n", a, b, (a && b));

   return 0;
}