#include<conio.h>
#include<iostream>
using namespace std;

class unary
{
private:
    int a;

public:
    void setData()
    {
        cout<<"Enter a number:  ";
        cin>>a;
    }
    void showData()
    {
        cout<<"Result is:  "<<a;
    }
    friend unary operator ++(unary);
};

unary operator ++(unary x)
{
    unary temp;
    temp.a=++x.a;
    return(temp);
}

int main()
{
    cout<<"Program to increment Any no. by 1.\n";
    unary u1,u2,u3;
    u1.setData();
    u2=++u1;                 //u2=operator++(u1);
    u2.showData();
    getch();
}
