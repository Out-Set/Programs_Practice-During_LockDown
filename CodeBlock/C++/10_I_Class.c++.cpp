#include<iostream>
using namespace std;

class person
{
private:
    int age,rollNo;
    char name[15],collegeName[50],stream[10];

public:
    void setData();
    void display();
};
void person::setData()
{
    cout<<"Enter Details of student:  \n\n";
    cout<<"Enter Name: \n";
    cin>>name;
    cout<<"Enter RollNo: \n";
    cin>>rollNo;
    cout<<"Enter Age: \n";
    cin>>age;
    cout<<"Enter CollegeName: \n";
    cin>>collegeName;
    cout<<"Enter Stream: \n";
    cin>>stream;
}
void person::display()
{
    cout<<"The details you entered:  "<<name<<" "<<rollNo<<" "<<age<<" "<<collegeName<<" "<<stream<<"\n";
}

int main()
{
    person p1,p2;
    p1.setData();
    p2.setData();
    p1.display();
    p2.display();
    return(0);
}
