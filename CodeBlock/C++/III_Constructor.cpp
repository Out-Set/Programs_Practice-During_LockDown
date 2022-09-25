#include<conio.h>
#include<iostream>
using namespace std;

class complex
{
private:
    int a,b;

public:
    complex(int x,int y)
    {
        cout<<"\nHello Constructor,";
        a=x; b=y;
        cout<<"\n a= "<<a<<",b= "<<b;
    }
};

int main()
{
    complex c1(3,4);//c2(); it will give an error, bcoz we didn't passed paremeters, yet after creating a constructor.
    return 0;
    getch();
}

