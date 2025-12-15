#include <iostream>
#include <string>
using namespace std;

void myFunction(string a, string country = "Norway") {
  cout << country << "\n";
}

int main() {
  myFunction("Sweden", "ABC");
  myFunction("India", "ABC");
  myFunction("ABCD", "ABC");
  myFunction("USA", "ABC");
  return 0;
}