#include<conio.h>
#include<iostream>
using namespace std;

class decrement
{
private:
    int a;

public:
    void setData()
    {
        cout<<"Enter a NO: ";
        cin>>a;
    }
    void showData()
    {
        cout<<"Result is: "<<a;
    }
    decrement operator ++()
    {
        decrement temp;
        temp.a=++a;
        return(temp);
    }
};

int main()
{
    cout<<"Program to Increment a no by 1.\n";
    decrement c1,c2;
    c1.setData();
    c2=++c1;
    //c2=c1.operator ++();
    c2.showData();
    getch();
}
