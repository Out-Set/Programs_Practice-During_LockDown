#include<conio.h>
#include<string.h>
#include<iostream>
#include<stdio.h>
using namespace std;

struct book
{
    int Bookid;
    char Title[20];
    float Price;
};
book input();
void display(book);
main()
{
   book b1;
   b1=input();
   display(b1);
   getch();
}
book input()
{
    book b;
    cout<<"Enter Bookid,Title,Price: \n";
    cin>>b.Bookid>>b.Title>>b.Price;
    return(b);
}
void display(book b)
{
    cout<<"\n";
    cout<<"\n"<<b.Bookid<<"  "<<b.Title<<"  "<<b.Price;
}
