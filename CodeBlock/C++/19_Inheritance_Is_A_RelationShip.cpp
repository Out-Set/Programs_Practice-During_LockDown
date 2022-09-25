#include<conio.h>
#include<iostream>
using namespace std;

// IS_A_RELATIONSHIP i.e. 1.Sports car is a car.  2.Banana is a fruit.  3.Round table is a table.  4.Table is a furniture.

// IS_A_RELATIONSHIP->Is always implemented as a Public Inheritance.

class car
{
private:
    int gear;

public:
    void setGear()
    {
        cout<<"Enter NO of gears: ";
        cin>>gear;
    }
    void incrementGear()
    {
        if(gear<4)
            gear++;
    }
    void showData()
    {
        cout<<"Resultant gear is:  "<<gear<<"\n";
    }
};

class sportsCar:public car
{
public:
    void cardata()
    {
        setGear();
        incrementGear();
        showData();
    }
};

int main()
{
    cout<<"Car data, Gears will be incremented by 1 if<4:  \n";
    sportsCar c1;
    c1.cardata();
    return 0;
    getch();
}
