#include <iostream>
using namespace std;

int main() {
   int a = 1, b = 2;
   cout << "a = " << a << "\n";
   a = a + 1;       cout << "a = " << a << "\n";
   a += 1;          cout << "a = " << a << "\n";
   ++a;             cout << "a = " << a << "\n";
   a++;             cout << "a = " << a << "\n";

   a = 1;
   b = a+1;         cout << "a = " << a <<", b = " << b << "\n";
   a = 1;
   b = ++a;         cout << "a = " << a <<", b = " << b << "\n";
   
   a = 1;
   b = a++ + a++ + a++;
   cout << "a = " << a <<", b = " << b << "\n";
   a = 1;
   b = ++a + ++a + ++a;
   cout << "a = " << a <<", b = " << b << "\n";
   return 0;
}