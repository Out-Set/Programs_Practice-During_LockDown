#include<conio.h>
#include<iostream>
using namespace std;

class complex
{
private:
    int a,b;
public:
    void setValue(int x,int y)
    {
        a=x; b=y;
        //OR
        /*cout<<"Enter values of a,b for complex no a+ib: \n";
        cin>>a>>b;*/
    }
    void showData()
    {
        cout<<"\n"<<a<<"+"<<b<<"i";
    }
};

//Member function can be declared outside the class body also.

/*void complex::setValue(int x,int y)
{
    a=x; b=y;
}*/

main()
{
    complex c1;
    c1.setValue(5,4);
    c1.showData();
    getch();
}
