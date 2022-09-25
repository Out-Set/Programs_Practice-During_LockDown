#include<conio.h>
#include<iostream>
using namespace std;
int add(int,int=0,int=2);
main()
{
    int a,b;
    cout<<"Enter two numbers:  \n";
    cin>>a>>b;
    cout<<"Sum is "<<add(a,b)<<"\n";

    int c;
    cout<<"Enter three numbers:  \n";
    cin>>a>>b>>c;
    cout<<"Sum is "<<add(a,b,c);
    getch();
}
int add(int x,int y,int z)
{
    return(x+y+z);
}
