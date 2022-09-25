#include<iostream>
#include<conio.h>
using namespace std;

class sub
{
private:
    int math=90,physics=77,chemistry=69;

public:
    void display()
    {
        cout<<"Maths = "<<math<<"\nPhysics = "<<physics<<"\nChemistry = "<<chemistry<<"\n";
    }
};

int main()
{
    sub s1;
    s1.display();
    return 0;
    getch();
}
