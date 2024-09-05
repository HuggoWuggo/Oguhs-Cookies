//  By Hugo Lewczak
#include <iostream>

using namespace std;

int getInput(int given) {
    cout << "Enter a time in seconds: ";
    cin >> given;

    return given;
}

int main() {
    int seconds, hours, minutes;
    
    if (!(seconds = getInput(seconds))){
        cerr << "PLEASE ENTER ONLY NUMBERS\n";
    }
    else {
        minutes = seconds / 60;
        hours = minutes / 60;
        cout << seconds << " seconds is equal to " << int(hours) << 
            " hours, " << int(minutes%60) << " minutes and " << int(seconds % 60)
            << " seconds";

        return 0;
        }
}
