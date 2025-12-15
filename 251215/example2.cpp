#include <iostream>
#include <string>
using namespace std;

class Rectangle {
  public:
  	int width, height;
    
    Rectangle(int w, int h) {
    	width = w;
        height = h;
    }
    
    int area() {
      return width * height;
    }
};

int main() {
  Rectangle r(3,4);
  cout << r.area();
}
