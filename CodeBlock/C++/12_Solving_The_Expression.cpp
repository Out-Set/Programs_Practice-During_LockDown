#include<iostream>
#include<conio.h>
using namespace std;

class expression
{
private:
    int x,a,b,c;

public:
    void setData()
    {
        cout<<"Enter the value of a,b,c for the expression, x=a/b-c: \n";
        cin>>a>>b>>c;
    }
    void showData()
    {
        x=a/b-c;
        cout<<"\n Result is: "<<x;
    }
};

int main()
{
    expression e1,e2;
    e1.setData();
    e2.setData();
    e1.showData();
    e2.showData();
    getch();
}
