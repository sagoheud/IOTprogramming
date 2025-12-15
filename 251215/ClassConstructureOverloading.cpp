#include <iostream>
using namespace std;

class Car {        // The class
  public:          // Access specifier
    string brand;  // Attribute
    string model;  // Attribute
    int year;      // Attribute
    Car(string brand, string model, int year) {
      this->brand = brand; //다른 언어에선 this.으로 사용
      this->model = model;
      this->year = year;
    }
    Car(string x, string y) {
      brand = x;
      model = y;
      year = 2025;
    }
    Car(string x) {
      brand = x;
      model = "Z";
      year = 2025;
    }
    Car() {
      brand = "V";
      model = "Z";
      year = 2025;
    }
};

int main() {
  // Create Car objects and call the constructor with different values
  Car carObj1("BMW", "X5", 1999);
  Car carObj2("Ford", "Mustang");
  Car carObj3("BMW");
  Car carObj4; //인자가 없는 생성자 호출시 괄호 생략 가능

  // Print values
  cout << carObj1.brand << " " << carObj1.model << " " << carObj1.year << "\n";
  cout << carObj2.brand << " " << carObj2.model << " " << carObj2.year << "\n";
  cout << carObj3.brand << " " << carObj3.model << " " << carObj3.year << "\n";
  cout << carObj4.brand << " " << carObj4.model << " " << carObj4.year << "\n";
  return 0;
}