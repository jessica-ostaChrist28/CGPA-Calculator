#include <iostream>
#include <iomanip>
using namespace std;

// Convert grade to grade point
int getGradePoint(string grade)
{
    if (grade == "O")
        return 10;
    if (grade == "A+")
        return 9;
    if (grade == "A")
        return 8;
    if (grade == "B+")
        return 7;
    if (grade == "B")
        return 6;
    if (grade == "C")
        return 5;
    return 0;
}

// Function to take input for one subject
void getSubjectData(int index, float &credit, string &grade)
{
    cout << "Subject " << index + 1 << " credit: ";
    cin >> credit;

    cout << "Grade: ";
    cin >> grade;
}

// Function to calculate CGPA
float calculateCGPA(int n)
{
    float totalCredits = 0;
    float totalPoints = 0;

    for (int i = 0; i < n; i++)
    {
        float credit;
        string grade;

        getSubjectData(i, credit, grade);

        int gp = getGradePoint(grade);

        totalCredits += credit;
        totalPoints += credit * gp;
    }

    return totalPoints / totalCredits;
}

// Function to display result
void displayResult(float cgpa)
{
    cout << "\n=== Your CGPA ===" << endl;
    cout << fixed << setprecision(2) << "CGPA: " << cgpa << endl;
}

// Main function
int main()
{
    int n;

    cout << "=== CGPA Calculator ===" << endl;
    cout << "Enter number of subjects: ";
    cin >> n;

    if (n <= 0)
    {
        cout << "Invalid number of subjects!\n";
        return 1;
    }

    float cgpa = calculateCGPA(n);

    displayResult(cgpa);

    return 0;
}