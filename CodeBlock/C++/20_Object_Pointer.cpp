#include<conio.h>
#include<iostream>
using namespace std;

class Box
{
private:
    int l,b,h;

public:
    void setDimension(int x,int y,int z)
    {
        l=x; b=y; h=z;
    }
    void showDimension()
    {
        cout<<"l="<<l<<"\nb="<<b<<"\nh="<<h;
    }
};

int main()
{
    Box *p,smallBox;
    p=&smallBox;
    p->setDimension(22,12,5);  // Pointer p is pointing to an object.
    p->showDimension();
    return 0;
    getch();
}
