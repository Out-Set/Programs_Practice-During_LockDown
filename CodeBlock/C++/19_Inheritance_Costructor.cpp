#include<conio.h>
#include<iostream>
using namespace std;

class A
{
    int b;

public:
    A(int k)
    {
        cout<<"Hello constructor!\n";
        b=k;
        cout<<"b="<<b<<" ";
    }
};

class B:public A
{
    int a;
public:
    B(int x,int y):A(x)
    {
        a=y;
        cout<<"a="<<a<<" \n";
    }
};

int main()
{
    cout<<"Constructor in Inheritance. \n";
    B obj(2,3);
    return 0;
    getch();
}
