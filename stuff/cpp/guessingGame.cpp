#include <iostream>
#include <time.h>

using namespace std;

int main() {
    int randomNum;

    srand(time(NULL));

    randomNum = rand() % 100 + 1;

    cout << randomNum << endl;
    
    int inp = 0;
  
    do {
        cout << "Enter a number: ";
        if (!(cin >> inp)) {
            cout << "Please enter a number" << endl;
            cin.clear();
            cin.ignore(1000, '\n');
        } else {
            if (inp > randomNum)
            {
                cout << "Too high!" << endl;
            }
            else if (inp < randomNum)
            {
                cout << "Too low!" << endl;
            }
        }
    } while (randomNum != inp);
    cout << "YOU GOT IT!" << endl;
    return 0;
}
