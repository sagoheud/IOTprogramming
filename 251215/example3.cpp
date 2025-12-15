#include <iostream>
using namespace std;

class BankAccount {
  private:
  	int balance;
    
  public:
  	BankAccount():balance(0) {}
    
    void deposit(int amount) {
    	balance += amount;
    }
    
    void withdraw(int amount) {
     	balance -= amount;
    }
    
    int getBalance() {
     	return balance;
    }
};

int main() {
	BankAccount acc;
  	acc.deposit(100);
  	acc.withdraw(30);
  	cout << acc.getBalance();
}
