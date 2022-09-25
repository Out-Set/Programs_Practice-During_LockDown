#include<iostream>
#include<conio.h>
using namespace std;

class largeOne
{
private:
    int a,b;

public:
    void compare()
        {
            if(a>b)
                cout<<a<<" is greatest\n";
            cout<<b<<" is greatest\n";
        }
    void setData()
        {
            cout<<"Enter two numbers, A and B:  \n";
            cin>>a>>b;
        }
};


main()
{
    largeOne l1;
    l1.setData();
    l1.compare();
    getch();
}
