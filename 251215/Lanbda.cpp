#include <iostream>
using namespace std;
 
int main() {
  auto message = []() {
    cout << "Hello World!\n";
  };

  message();
  return 0;
}