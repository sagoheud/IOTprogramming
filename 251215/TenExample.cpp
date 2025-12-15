//1. 정수 두 개를 입력받아 합,차,곱,몫을 출력
#include <iostream>
using namespace std;
int main() {
    int a, b;
    cin >> a >> b;
    cout << "합: " << a + b << "\n";
    cout << "차: " << a - b << "\n";
    cout << "곱: " << a * b << "\n";
    if (b != 0) {
        cout << "몫: " << a / b;
    } else {
        cout << "몫: 정의되지 않음 (0으로 나눌 수 없음)";
    }
    return 0;
}

//2. 정수 하나를 입력받아 양수/음수/0중 무엇인지 출력
#include <iostream>
using namespace std;
int main() {
    int a;
    cin >> a;
    if (a > 0) {
        cout << "양수";
    } else if (a < 0) {
        cout << "음수";
    } else {
        cout << "0";
    }
}

//3. 정수 N을 입력받아 1부터 N까지의 합 출력
#include <iostream>
using namespace std;
int main() {
    int N;
    cin >> N;
    int sum = 0;
    for (int i = 1; i <= N; i++) {
        sum += i;
    }
    cout << "1부터 " << N << "까지의 합: " << sum;
}

//4. 정수 5개를 입력받아 최대값,최소값 출력
#include <iostream>
using namespace std;
int main() {
    int arr[5];
    for (int i = 0; i < 5; i++) {
        cin >> arr[i];
    }
    int max = arr[0];
    int min = arr[0];
    for (int i = 0; i < 5; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    cout << "최대값: " << max << ", 최소값: " << min;
}

//5. 정수 두 개를 매개변수로 받아 큰 값을 반환하는 함수 maxValue 작성
#include <iostream>
using namespace std;
int maxValue(int a, int b) {
    return (a > b) ? a : b;
}
int main() {
    int x, y;
    cin >> x >> y;
    cout << "큰 값: " << maxValue(x, y);
}

//6. 학생 정보를 저장하는 Student 구조체를 만들고, 이름, 점수를 저장한 뒤 출력
#include <iostream>
using namespace std;
struct Student {
    string name;
    int score;
};
int main() {
    Student s{"홍길동", 95};
    cout << "이름: " << s.name << ", 점수: " << s.score;
}

//7. Book 클래스를 만들고 제목, 가격을 저장하고 출력하는 멤버 함수를 작성
#include <iostream>
using namespace std;
class Book {
    string title;
    int price;
    public:
        Book(string t, int p): title(t), price(p) {}

        void printInfo() {
            cout << "제목: " << title << ", 가격: " << price;
        }
};
int main() {
    Book b("C++ Programming", 30000);
    b.printInfo();
}

//8. point 클래스: x,y 좌표를 저장하고 두 점 사이의 거리를 출력
#include <iostream>
#include <cmath>
using namespace std;
class Point {
    double x, y;
    public:
        Point(double x, double y): x(x), y(y) {}

        double distanceTo(Point& other) {
            return sqrt(pow(x - other.x, 2) + pow(y - other.y, 2));
        }
};
int main() {
    Point p1(1.0, 2.0);
    Point p2(4.0, 6.0);
    cout << "두 점 사이의 거리: " << p1.distanceTo(p2);
}

//9. Animal 클래스: 함수 sound()로 Dog 클래스가 상속받아 "Dog barks" 출력
#include <iostream>
using namespace std;
class Animal {
    public:
        void sound() {
            cout << "Animal makes a sound";
        }
};
class Dog : public Animal {
    public:
        void sound() {
            cout << "Dog barks";
        }
};
int main() {
    Dog d;
    d.sound();
}

//10. 가상함수 (다형성): 문제 9를 확장하여 Animal* 포인터로 Dog 객체를 가리킬 때
// Dog의 sound()가 호출되도록 작성
#include <iostream>
using namespace std;
class Animal {
    public:
        virtual void sound() {
            cout << "Animal makes a sound";
        }
};
class Dog : public Animal {
    public:
        void sound() {
            cout << "Dog barks";
        }
};
int main() {
    Animal* a;
    Dog d;
    a = &d;
    a->sound(); // "Dog barks" 출력
}
