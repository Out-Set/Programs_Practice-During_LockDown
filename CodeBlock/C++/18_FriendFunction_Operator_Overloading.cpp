#include<conio.h>
#include<iostream>
using namespace std;

class complex
{
private:
    int a,b;

public:
    void setData()
    {
        cout<<"Enter the values of A and B for, a+ib: \n";
        cin>>a>>b;
    }
    void showData()
    {
        cout<<"Result is: "<<a<<"+"<<b<<"i";
    }
    friend complex operator +(complex,complex);
};

complex operator +(complex x,complex y)
{
    complex temp;
    temp.a=x.a+y.a;
    temp.b=x.b+y.b;
    return(temp);
}

int main()
{
    cout<<"Program for Adding two ComplexNo.\n";
    complex c1,c2,c3;
    c1.setData();
    c2.setData();
    c3=c1+c2;
    c3.showData();
    getch();
}
