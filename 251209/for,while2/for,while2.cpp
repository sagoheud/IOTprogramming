#include <iostream>
using namespace std;

int main() {
    int i = 1;

    for(;;i++){
        if(i == 10)
            break;
        cout << "Hello CPP World!!\n";
    }

    while(1)
    {
        if(i == 5)
            break;
        cout << "Hello Control Statement World!!\n";
        i--;
    }

   return 0;
}