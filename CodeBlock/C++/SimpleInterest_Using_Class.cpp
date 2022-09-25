#include<conio.h>
#include<iostream>
using namespace std;

class simpleInterest
{
private:
    int p,r,t;
    float si;

public:
    void setData()
    {
        cout<<"Enter data P,R,T for calculation of SI: \n";
        cin>>p>>r>>t;
    }
    void calculate()
    {
        si=(p*r*t)/100;
        cout<<"Simple Interest is:    "<<si;
    }
};
 main()
 {
     simpleInterest s1;
     s1.setData();
     s1.calculate();

 }
