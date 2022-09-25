#include<iostream>
#include<conio.h>
using namespace std;

class ASCII
{
private:
    char c;

public:
    void setData()
    {
        cout<<"Program to print ACSII value of any character/Special symbols.\n";
        cout<<"Enter a character:  \n";
        cin>>c;
    }
    void showData()
    {
        cout<<"\n ASCII value of "<<c<<" is: "<<(int)c;
    }
};

main()
{
    ASCII a1;
    a1.setData();
    a1.showData();
    getch();
}
