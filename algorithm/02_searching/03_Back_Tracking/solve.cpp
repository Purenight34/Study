#include <iostream>
#include <vector>

using namespace std;
vector<int> points;

void fistOfTheNorthStar(vector<int>& arr, int start, int remaining)
{
  if(remaining == 0)
  {
    if(arr[0] == 1 && arr.back() == 1) return;
    for(int x : arr) cout << x;
    cout << "\n";
    return;
  }

  for(int i = start; i < arr.size(); i++)
  {
    arr[i] = 1;
    fistOfTheNorthStar(arr, i + 1, remaining - 1);
    arr[i] = 0;
  }
  return;
}
int main()
{
  int n, m;
  cin >> n >> m;
  vector<int> points (n, 0);
  fistOfTheNorthStar(points, 0, m);
  return 0;
}