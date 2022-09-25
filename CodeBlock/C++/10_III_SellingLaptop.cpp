#include<conio.h>
#include<iostream>
using namespace std;

class Laptop
{
private:
    char brand[20],model[20];
    int price;

public:
    void laptops()
    {
        cout<<laptop1<<laptop2<<laptop3<<laptop4<<laptop5;
    }
    void chooselaptop()
    {

    }
    void applyDiscount()
    {
        cout<<"Please enter discount in Precentage:  ";
        cin>>discount;
    }
};

    Laptop l1={"Lenovo" "ideapad 330" 42500};
    Laptop l2={"Lenovo" "ideapad 130" 35500};
    Laptop l3={"Dell" "inspiration 42000" 66500};
    Laptop l4={"Lenovo" "thinkpad" 76500};
    Laptop l5={"Apple" "Imac" 105500};
