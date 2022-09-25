#include<conio.h>
#include<iostream>
using namespace std;

class tempConversion
{
private:
    int fahr;
    float celc;

public:
    void setData()
    {
        cout<<"Enter temprature in Fahrenhiet:  \n";
        cin>>fahr;
    }
    void showData()
    {
        celc=(5*(fahr-32))/9;
        cout<<"\nResult is: "<<celc<<"*c";
    }
};

main()
{
    tempConversion t1;
    t1.setData();
    t1.showData();
    getch();
}
