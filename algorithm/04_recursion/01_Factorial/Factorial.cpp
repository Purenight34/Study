#include <iostream>

using namespace std;

long long int factorial(int number)
{
  if(number == 0 || number == 1)
  {
    return 1;
  }
  return number * factorial(number - 1); 
}

int main()
{
  long long int number;
  cin >> number;
  cout << factorial(number);
  return 0;
}