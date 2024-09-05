//  By Hugo Lewczak
#include <iostream>

using namespace std;

void UserInput(float *ass1, float *ass2, float *ass3, float *ass4, float *midterm, float *final, float *par) {
    cout << "Enter the score for the first assignment: ";
    cin >> *ass1;
    cout << "Enter the score for the second assignment: ";
    cin >> *ass2;
    cout << "Enter the score for the third assignment: ";
    cin >> *ass3;
    cout << "Enter the score for the fourth assignment: ";
    cin >> *ass4;
    cout << "Enter the score for midterm: ";
    cin >> *midterm;
    cout << "Enter the score for final: ";
    cin >> *final;
    cout << "Enter the score for participation: ";
    cin >> *par;
}

float Assignments(float *ass1, float *ass2, float *ass3, float *ass4) {
    float average;

    average = (*ass1 + *ass2 + *ass3 + *ass4) / 4 * 0.4;

    return average;
}

float Midterm(float *mid) {
    float result = *mid * 0.15;
    return result;
}

float Final(float *final) {
    float result = *final * 0.35;
    return result;
}

float ClassParticipation(float *par) {
    float result = *par * 0.1;
    return result;
}

int main() {
    float ass1, ass2, ass3, ass4, midterm, final, par;
    float markAss, markMid, markF, markPas;
    float finalGrade;

    UserInput(&ass1, &ass2, &ass3, &ass4, &midterm, &final, &par);
    markAss = Assignments(&ass1, &ass2, &ass3, &ass4);
    markMid = Midterm(&midterm);
    markF = Final(&final);
    markPas = ClassParticipation(&par);

    finalGrade = markAss + markF + markMid + markPas;

    cout << "The final grade is: " << finalGrade << endl;

    return 0;
}
