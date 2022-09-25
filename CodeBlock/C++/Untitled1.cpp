#include<conio.h>
#include<iostream>
using namespace std;
int main()
{
    int a,b;
	cout<<"Hello World!\n";
	cout<<"Program to swap to numbers.\n";
	cout<<"\n";
	cout<<"Enter two numbers\n";
	cin>>a>>b;
	cout<<"Before swapping: "<<"a="<<a<<" & b="<<b<<"\n";
	b=((a+b)-(a=b));
	cout<<"After swapping: "<<"a="<<a<<" & b="<<b;
	return 0;
	getch();
}
