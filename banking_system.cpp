#include <iostream>
#include <vector>
#include <string>

using namespace std;

// 1. Transaction Class
class Transaction {
public:
    string type;
    double amount;

    Transaction(string t, double amt) {
        type = t;
        amount = amt;
    }

    void displayTransaction() {
        cout << "- " << type << ": Rs. " << amount << endl;
    }
};

// 2. Account Class
class Account {
private:
    string accountNumber;
    double balance;
    vector<Transaction> history; // Transaction history store karne ke liye vector

public:
    Account(string accNum, double initialBalance) {
        accountNumber = accNum;
        balance = initialBalance;
    }

    string getAccountNumber() { return accountNumber; }
    double getBalance() { return balance; }

    // Deposit Feature
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            history.push_back(Transaction("Deposit", amount));
            cout << "Rs. " << amount << " kamyabi se jama ho gaye hain.\n";
        }
    }

    // Withdraw Feature
    bool withdraw(double amount) {
        if (amount > balance) {
            cout << "Incomplete Transaction! Aapka balance kam hai.\n";
            return false;
        } else if (amount <= 0) {
            return false;
        } else {
            balance -= amount;
            history.push_back(Transaction("Withdrawal", amount));
            cout << "Rs. " << amount << " nikal liye gaye hain.\n";
            return true;
        }
    }

    // History Display Feature
    void displayHistory() {
        cout << "\n--- Transaction History for Acc: " << accountNumber << " ---\n";
        if (history.empty()) {
            cout << "Koi transaction nahi hui.\n";
        } else {
            for (int i = 0; i < history.size(); i++) {
                history[i].displayTransaction();
            }
        }
        cout << "Current Balance: Rs. " << balance << endl;
    }
};

// 3. Customer Class
class Customer {
public:
    string name;
    string customerID;
    Account account; // Customer ka apna account

    Customer(string n, string id, string accNum, double initialBalance) 
        : name(n), customerID(id), account(accNum, initialBalance) {}

    void displayCustomerInfo() {
        cout << "\n=====================================" << endl;
        cout << "Customer Name: " << name << "\nID: " << customerID << endl;
        cout << "Account Number: " << account.getAccountNumber() << endl;
        cout << "Available Balance: Rs. " << account.getBalance() << endl;
        cout << "=====================================" << endl;
    }
};

int main() {
    // Demo ke liye do customers create karte hain
    Customer c1("Sadia", "C101", "PK78692", 50000.0);
    Customer c2("Ayesha", "C102", "PK78695", 20000.0);

    cout << "--- Banking System Simulation ---\n";
    c1.displayCustomerInfo();

    // 1. Test Deposit
    cout << "\n[Action] Sadia apne account mein Rs. 10,000 jama kar rahi hain:\n";
    c1.account.deposit(10000);

    // 2. Test Withdrawal
    cout << "\n[Action] Sadia Rs. 5,000 nikal rahi hain:\n";
    c1.account.withdraw(5000);

    // 3. Test Fund Transfer (Sadia se Ayesha ko)
    double transferAmount = 15000;
    cout << "\n[Action] Sadia Rs. " << transferAmount << " Ayesha ko transfer kar rahi hain:\n";
    if (c1.account.withdraw(transferAmount)) {
        c2.account.deposit(transferAmount);
        cout << "Transfer Successful!\n";
    }

    // 4. Final Display aur Statements
    cout << "\n--- Updated Account Status ---\n";
    c1.displayCustomerInfo();
    c1.account.displayHistory();

    c2.displayCustomerInfo();
    c2.account.displayHistory();

    return 0;
}
