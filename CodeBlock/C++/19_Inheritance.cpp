#include<conio.h>
#include<iostream>
using namespace std;

class A
{
private:
    int a,b;

protected:
    void setData(int k)
    {
        a=k;
    }
    void showData()
    {
        cout<<"Data is: "<<a<<"\n";
    }
};

class B:public A
{
public:
    void setValue(int x)
    {
        setData(x);     // We accessed the protected member functions of class A, inside class B through inheritance.
        showData();     // Same here.
    }
};

int main()
{
    B obj;
    obj.setValue(5);
    //obj.showData();     // Show an error bcoz it's a protected member of class A.
    return 0;
    getch();
}
