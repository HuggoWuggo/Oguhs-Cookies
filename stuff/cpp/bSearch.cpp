// efficiency 0(log n)
#include <iostream>
#include <vector>
#include <algorithm>

int binary(std::vector<int> arr, int low, int high, int target) {
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (mid == target)
            return mid;

        if (mid > target)
            high = mid -1;

        if (mid < target)
            low = mid + 1;

        std::cout << "Step is: " << mid << std::endl;

    }
    return -1;
}


int main() {
    long long int end, x;

    try {
        std::cout << "Enter the range: ";
        if (!(std::cin >> end)) {
            throw(end);
        } else {
            std::cout << "Enter the target: ";
            if (!(std::cin >> x)) {
                throw(x);
            }
            else if (x > end) {
                std::cout << "Target is greater than range" << std::endl;
            }
            else {
                std::vector<int> v;

                for ( int i = 1; i <= end; i++ ) {
                    v.push_back( i );
                }
                int index = binary(v, v[0], end -1, x);
                
                if (index == -1) {
                    std:: cout << "Number not found" << std::endl;
                } else {
                    std::cout << "Number found at index: " << index << std::endl;
                }
            }
        }
    }

    catch(long long int myNum) {
        std::cout << "Please enter a number" << std::endl;
    }
}