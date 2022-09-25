#include<conio.h>
#include<iostream>
using namespace std;

class complex
{
private:
    int a,b;

public:
    //If you don't create a constructor, it's ok compiler will create a default constructor(or Implicit default constructor)
    //you will get no error.

    //But incase you want to pass argument, you must have to create a constructor.
    //Once you created a constructor, compiler won't create a default constructor.
};

int main()
{
    complex c1,c2,c3,c4,c5;
    return 0;
    getch();
}
