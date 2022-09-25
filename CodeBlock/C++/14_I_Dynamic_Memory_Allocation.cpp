#include<conio.h>
#include<iostream>
#include<istream>
using namespace std;
main()
{
    int *arr,i;
    int size;

    cout<<"Enter the size of the integer array: \n";
    cin>>size;

    cout<<"Creating an array of size /n"<<size<<"..";
    arr=new int[size];

    for(i=1;i<=size;i++)
    {
        cout<<"Enter "<<size<<" value for array: \n";
        cin>>arr;
    }
    for(i=1;i<=size;i++)
    {
        cout<<"\nArray values are: "<<arr;
    }

    cout<<"\nDynamic allocation of memory for array is successful.";

    delete arr;
    getch();
}
