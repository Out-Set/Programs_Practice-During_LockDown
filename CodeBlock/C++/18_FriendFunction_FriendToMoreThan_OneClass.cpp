#include<conio.h>
#include<iostream>
using namespace std;

class B; //Forward declaration of class B, for complier to make understand the meaning of B.

class A
{
private:
    int a;

public:
    void setData()
    {
        cout<<"Enter 1stNo: ";
        cin>>a;
    }
    friend void fun(A,B);          //Friend of Class A & B
};

class B
{
private:
    int b;

public:
    void setData()
    {
        cout<<"Enter No: ";
        cin>>b;
    }
    friend void fun(A,B);           //Friend of Class A & B
};

void fun(A o1,B o2)
{
    cout<<"Sum is:  "<<o1.a+o2.b;
}

main()
{
    cout<<"Program to add Two Numbers: \n";
    A obj1;
    B obj2;
    obj1.setData();
    obj2.setData();
    fun(obj1,obj2);
    getch();
}
