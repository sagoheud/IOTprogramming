#include <iostream>
using namespace std;

void myFunction(){
    cout << "I just got executed\n";
    return;
}
void yourFunction(){
    cout << "I just got executed too!\n";
    return;
}

int main() {
    myFunction();
    yourFunction();
    return 0;
}
