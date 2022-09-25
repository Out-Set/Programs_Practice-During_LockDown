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
        cout<<"Enter the values of a and b: \n";
        cin>>a>>b;
    }
    void showData()
    {
        cout<<"Result is:  "<<a<<"+"<<b<<"i";
    }
    complex add(complex c)
    {
        complex temp;
        temp.a=a+c.a;
        temp.b=b+c.b;
        return(temp);
    }
};
main()
{
    complex c1,c2,c3;
    c1.setData();
    c2.setData();
    c3=c1.add(c2);
    c3.showData();
    getch();
}
