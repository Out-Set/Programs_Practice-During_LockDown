#include<conio.h>
#include<iostream>
using namespace std;

class complex
{
private:
    int a,b;

public:
    complex(int x,int y)  //parameterized constructor
    {
        cout<<"\nHello Constructor  \n\n";
        a=x; b=y;
        cout<<"a= "<<a<<",b= "<<b;
    }
    complex(int z)       //parameterized constructor
    {
    a=z;
    cout<<"\n\na= "<<a;
    }

    complex()  //default constructor
    {
    a=0; b=0;
    cout<<"\n\na= "<<a<<",b= "<<b;
    }

};

int main()
{
    complex c1(5,6);
    complex c2(2),c3=5;
    complex c4=complex(8,9),c5=complex(7),c6;
    return 0;
    getch();
}

