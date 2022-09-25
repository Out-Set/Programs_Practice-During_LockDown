#include<conio.h>
#include<iostream>
using namespace std;
main()
{
    int a=5;
    int *p,**q,***r;
    p=&a;
    q=&p;
    r=&q;

    cout<<a<<"\n";
    cout<<&a<<"\n";
    cout<<"\n";

    cout<<p<<"\n";
    cout<<&p<<"\n";
    cout<<*p<<"\n";
    cout<<"\n";

    cout<<q<<"\n";
    cout<<&q<<"\n";
    cout<<*q<<"\n";
    cout<<**q<<"\n";
    cout<<"\n";

    cout<<r<<"\n";
    cout<<&r<<"\n";
    cout<<*r<<"\n";
    cout<<**r<<"\n";
    cout<<***r<<"\n";
    cout<<"\n";

    getch();
}
