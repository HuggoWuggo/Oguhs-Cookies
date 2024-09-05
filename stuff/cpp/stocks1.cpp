//  By Hugo Lewczak
// Helped by Thomas Mclean
#include <iostream>
#include <vector>

using namespace std;

int maxProfit(vector<int>& prices) {
        int minprice = INT_MAX;
        int maxprofit = 0;
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
}

int main() {
  vector<int> arr = {/*put your arrray*/2, 100, 3, 1, 10};
  int result = maxProfit(arr);
  if (result == 0) {
    cout << "No profit made" << endl;
  } else {
    cout << "Your profit is: "<< result << endl;
  }
  return 0;
}
