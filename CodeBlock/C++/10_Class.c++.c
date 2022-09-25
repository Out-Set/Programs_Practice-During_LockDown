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
        x=a; y=b;
    }
    void showData()
    {
        cout<<"\n"<<a<<"+i"<<b;
    }
};

main()
{
    Complex c1;
    c1.setValue(3,4);
    c1.showData();
    getch();
}
