#include<conio.h>
#include<iostream>
using namespace std;

class add_Using_Friend_Function
{
private:
    int a,b;

public:
    void setData()
    {
        cout<<"Enter two numbers: \n";
        cin>>a>>b;
    }
    friend void fun(add_Using_Friend_Function c);  //Uses keywords 'Friend'
};

void fun(add_Using_Friend_Function x)              //Must be defined outside of the class.
{
    cout<<"Sum is: "<<x.a+x.b;
}

int main()
{
    cout<<"Program to add two numbers.\n";
    add_Using_Friend_Function add1;
    add1.setData();
    fun(add1);
    return 0;
    getch();
}
