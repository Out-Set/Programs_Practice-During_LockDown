
#include<conio.h>
#include<iostream>
using namespace std;

class A
{
public:
    ~A()
    {
        cout<<"Hello constructor!\n";
    }
};

class B:public A
{
public:
    ~B()
    {

    }
};

int main()
{
    cout<<"Distructor in Inheritance. \n";
    B obj();
    return 0;
    getch();
}
