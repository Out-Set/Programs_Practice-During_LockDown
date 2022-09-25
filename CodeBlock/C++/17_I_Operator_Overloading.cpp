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
        cout<<"Enter the values of a and b, for complex no a+ib:  \n";
        cin>>a>>b;
    }
    void showData()
    {
        cout<<"Result is: "<<a<<"+"<<b<<"i";
    }
    complex operator +(complex c)  // Use 'operator' keywords with operator's sign....but you can't overload sizeof() and ?: operator.
    {
        complex temp;
        temp.a=a+c.a;
        temp.b=b+c.b;
        return(temp);
    }
};

main()
{
    cout<<"Program to add two complexNo.\n";
    complex c1,c2,c3;
    c1.setData();
    c2.setData();
    c3=c1+c2;                 // OR c3=c1.add(c2);
    //c3=c1.operator+(c2);
    c3.showData();
    getch();
}
