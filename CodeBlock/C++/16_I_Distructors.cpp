#include<conio.h>
#include<iostream>
using namespace std;


class complex
{
private:
    int a,b;

public:
    ~complex()  // A distructor has no return type, as well as no argument.
    {
        cout<<"I am a distructor.\n";
    }
};

void fun()
{
    complex obj;
}

main()
{
    fun();
    fun();
    getch();
}
