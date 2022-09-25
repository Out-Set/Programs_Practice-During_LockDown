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
        this->l=x; this->b=y; this->h=z;
        //l=x; b=y; h=z;
    }
    void showData()
    {
        cout<<"l="<<l<<"\nb="<<b<<"\nh="<<h;
    }
};

int main()
{
    Box smallBox;
    smallBox.setDimension(12,5,6);
    smallBox.showData();
    return 0;
    getch();
}
