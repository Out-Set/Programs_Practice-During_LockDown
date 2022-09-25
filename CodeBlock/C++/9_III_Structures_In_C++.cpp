#include<conio.h>
#include<iostream>
using namespace std;

class book
{
private:
    int Bookid;
    char Title[20];
    float Price;

public:
    void input()
    {
        cout<<"Enter Bookid,Title,Price: \n";
        cin>>Bookid>>Title>>Price;
    }
    void display()
    {
        cout<<"\n";
        cout<<Bookid<<" "<<Title<<" "<<Price;
    }
};

main()
{
    book b1;
    //b1.Bookid=25; It is a private member of book class, Anyone can't access it. Only input()& display() are accessible.
    b1.input();
    b1.display();
    getch();
}
