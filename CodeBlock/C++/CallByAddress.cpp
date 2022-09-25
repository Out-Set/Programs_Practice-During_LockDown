#include<conio.h>
#include<iostream>
using namespace std;
int sum(int *,int *);
main()
{
    int a,b,s;
    cout<<"Enter two numbers: \n";
    cin>>a>>b;
    s=sum(&a,&b);
    cout<<"Sum of "<<a<<" and "<<b<<" is "<<s;
    getch();
}
int sum(int *x,int *y)
{
    return(*x+*y);
}
