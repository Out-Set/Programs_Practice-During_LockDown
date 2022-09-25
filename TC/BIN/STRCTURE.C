#include<stdio.h>
struct student
{
 char name[20];
 int rollno;
 float marks;
};
int main(void)
{
 struct student stu1={"ram",25,51};
 struct student stu2,stu3;
 stu2.name={"shyam"};
 stu2.rollno=26;
 stu2.marks=98;
 printf("enter name,rollno & marks for student 3\n");
 scanf("%s%d%f",&stu3.name,&stu3.rollno,&stu3.marks);
 printf("stu1\t%s\t%d\t%2f\n",stu1.name,stu1.rollno,stu1.marks);
 printf("stu2\t%s\t%d\t%2f\n",stu2.name,stu2.rollno,stu2.marks);
 printf("stu3\t%s\t%d\t%2f\n",stu3.name,stu3.rollno,stu3.marks);
 getch();
 return 0;
}
