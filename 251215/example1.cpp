#include <iostream>
#include <string>
using namespace std;

class Person {
	public:
		string name; //variable
    	int age;
    
        void print() {
            cout << name << ", " << age;
        }  //method
};


int main() {
	Person p;
    p.name = "진";
    p.age = 24;
	p.print();
}