// 두 이차원 배열의 합을 구하는 프로그램을 작성하시오.
// 단 이차원 배열의 행과 열은 같다고 가정한다
// arr1의 내용을 화면에 출력하고, arr2의 내용을 화면에 출력하고
// 두 배열의 합을 화면에 출력한다
#include <iostream>
using namespace std;

int main() {
    int i,j;
    int arr1[2][5] = {{1, 2, 3, 4, 5},{6, 7, 8, 9, 10}};
    int arr2[2][5] = {{9, 8, 7, 6, 5},{1, 2, 3, 4, 5}};

    //arr1 출력
    for (i = 0; i < sizeof(arr1)/sizeof(arr1[0]); i++){
        for (j = 0; j < sizeof(arr1[0])/sizeof(arr1[0][0]); j++){  
            cout << arr1[i][j] << " ";
        }
    }
    cout << "\n";

    //arr2 출력
    for (i = 0; i < sizeof(arr2)/sizeof(arr2[0]); i++){
        for (j = 0; j < sizeof(arr2[0])/sizeof(arr2[0][0]); j++){  
            cout << arr2[i][j] << " ";
        }
    }
    cout << "\n";

    //arr3 생성 및 출력
    int arr3[2][5];
    for (i = 0; i < sizeof(arr1)/sizeof(arr1[0]); i++){
        for (j = 0; j < sizeof(arr1[0])/sizeof(arr1[0][0]); j++){  
            arr3[i][j] = arr1[i][j] + arr2[i][j];
            printf("%3d", arr3[i][j]);
        }
    }
    

    // cout << sizeof(arr1) << "\n";
    // cout << sizeof(arr1[0]) << "\n";
    // cout << sizeof(arr1[0][0]) << "\n";
    // cout << sizeof(arr1)/sizeof(arr1[0]) << "\n";
    // cout << sizeof(arr1[0])/sizeof(arr1[0][0]) << "\n";
 
    return 0;
}