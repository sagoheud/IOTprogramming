#include <iostream>
using namespace std;

int main() {
   int a;

   cout << "정수 입력: ";
   cin >> a;

//    if(a%3){
//     cout << "3의 배수가 아닙니다."; //내용이 여러줄 일 땐 중괄호
//    }
//    else{
//     cout << "3의 배수입니다.";
//    }

   if(++a%3)
    cout << "3의 배수가 아닙니다.";
   
   else
    cout << "3의 배수입니다.";
   

   return 0;
}