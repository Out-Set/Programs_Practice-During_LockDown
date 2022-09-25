#include<conio.h>
#include<iostream>
using namespace std;
struct book
{
    int Bookid;
    char Title[20];
    float price;

    void input()
    {
        cout<<"Enter Bookid,Title,Price: \n";
        cin>>Bookid>>Title>>price;
    }
    void display()
    {
        cout<<"\n";
        cout<<Bookid<<" "<<Title<<" "<<price;
    }
};

main()
{
    book b1;
    //b1.Bookid=20; anyone can access these field...to resolve see 9_III_Structures_In_C++
    b1.input();
    b1.display();
    getch();
}
