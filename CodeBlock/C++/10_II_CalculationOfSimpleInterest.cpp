#include<conio.h>
#include<iostream>
using namespace std;

class SI
{
private:
    int p,t;
    float r,res;

public:
    void showData()
    {
        res=(p*r*t)/100;
        cout<<"SI is:  "<<res;
    }
    void setData()
    {
        cout<<"Program to calculate Simple-Interest.\n";
        cout<<"Enter the values of P,R,T:  \n";
        cin>>p>>r>>t;
    }

};

main()
{
    SI si1;
    si1.setData();
    si1.showData();
    getch();
}
