#include <iostream>
#include <fstream>
using namespace std;

// Function to take input
void getInput(string &username, string &password)
{
    cout << "Enter username: ";
    cin >> username;

    cout << "Enter password: ";
    cin >> password;
}

// Function to save user (Signup)
void saveUser(string username, string password)
{
    ofstream file("data/users.txt", ios::app);
    file << username << " " << password << endl;
    file.close();
}

// Function to check login
bool checkLogin(string username, string password)
{
    ifstream file("data/users.txt");
    string u, p;

    while (file >> u >> p)
    {
        if (u == username && p == password)
        {
            return true;
        }
    }
    return false;
}

// Signup function
void signup()
{
    string username, password;

    getInput(username, password);
    saveUser(username, password);

    cout << "Signup successful!\n";
}

// Login function
void login()
{
    string username, password;

    getInput(username, password);

    if (checkLogin(username, password))
    {
        cout << "Login successful!\n";
    }
    else
    {
        cout << "Invalid credentials!\n";
    }
}

int main()
{
    int choice;

    cout << "1. Signup\n2. Login\nChoice: ";
    cin >> choice;

    switch (choice)
    {
    case 1:
        signup();
        break;
    case 2:
        login();
        break;
    default:
        cout << "Invalid choice!";
    }

    return 0;
}