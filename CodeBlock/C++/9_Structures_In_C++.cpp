#include<conio.h>
#include<iostream>
#include<string.h>
using namespace std;

struct  book
{
    int Bookid;
    char Title[20];
    float price;
}b1;

struct book b2={2,"Concept of physics",350.00};

main()
{
    book b3,b4;
    b1.Bookid=1;
    strcpy(b1.Title,"JAVA");
    b1.price=470.00;

    cout<<"Enter Bookid,Title,Price:  \n";
    cin>>b3.Bookid>>b3.Title>>b3.price;

    b4=b3;

    cout<<"The Books-Records we have:   \n\n";
    cout<<"1."<<" "<<b1.Bookid<<"   "<<b1.Title<<"   "<<b1.price<<"\n";
    cout<<"2."<<" "<<b2.Bookid<<"   "<<b2.Title<<"   "<<b2.price<<"\n";
    cout<<"3."<<" "<<b4.Bookid<<"   "<<b4.Title<<"   "<<b4.price<<"\n";

    getch();

}
