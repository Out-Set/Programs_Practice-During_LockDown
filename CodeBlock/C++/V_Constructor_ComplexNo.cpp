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
        a=x; b=y;
    }
    complex(int z)
    {
        a=z; b=0;
    }
    complex()
    {

    }
    complex(complex &c)
    {
        a=c.a;
        b=c.b;
        cout<<"\nComplexNo is: "<<a<<"+"<<b<<"i";
    }
};

main()
{
    complex c1(2,3),c2(4),c3;
    complex c4(c1);
    getch();
}
