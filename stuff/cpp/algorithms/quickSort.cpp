// By Hugo Lewczak

#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int>& arr, int start, int end) {
    int pivot = arr[end];
    int i = start - 1;

    for (int j = start; j <= end - 1; j++) { // Corrected loop condition
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    i++;
    int temp = arr[i];
    arr[i] = arr[end];
    arr[end] = temp;

    return i;
}

void quickSort(vector<int>& arr, int start, int end) {
    if (end <= start) return; // base case

    int pivot = partition(arr, start, end);
    quickSort(arr, start, pivot - 1);
    quickSort(arr, pivot + 1, end);
}

int main() {
    vector<int> arr = {9, 4, 10, 2, 7, 6, 3, 8, 1, 5};

    quickSort(arr, 0, arr.size() - 1);

    for (int i : arr) {
        cout << i << " "; // Fixed output
    }
    cout << endl; // Added for cleaner output

    return 0;
}