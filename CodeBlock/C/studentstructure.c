#include <stdio.h>
#include <conio.h>
struct student
{
	char name[20],father[20];
	int rollno,enrollment;
	float marks;
};
void main()
{
	int i,n=3;
	struct student stu1,stu2,stu3;
	for(i=0;i<=3;i++)
	{
	
	printf("enter the student name,father name,roll no,enrollment no,marks\n");
	scanf("%s%s%d%d%f",&stu1.name,&stu1.father,&stu1.rollno,&stu1.enrollment,&stu1.marks);
	printf("enter the student name,father name,roll no,enrollment no,marks\n");
	scanf("%s%s%d%d%f",&stu2.name,&stu2.father,&stu2.rollno,&stu2.enrollment,&stu2.marks);
	printf("enter the student name,father name,roll no,enrollment no,marks\n");
	scanf("%s%s%d%d%f",&stu3.name,&stu3.father,&stu3.rollno,&stu3.enrollment,&stu3.marks);
	printf("STUDENT NAME\tFATHER NAME\tROLL NO\tENROLLMENT NO\tMARKS\n");
	printf("%s\t\t%s\t\t%d\t\t%d\t%f\n",stu1.name,stu1.father,stu1.rollno,stu1.enrollment,stu1.marks);
	printf("%s\t\t%s\t\t%d\t\t%d\t%f\n",stu2.name,stu2.father,stu2.rollno,stu2.enrollment,stu2.marks);
	printf("%s\t\t%s\t\t%d\t\t%d\t%f\n",stu3.name,stu3.father,stu3.rollno,stu3.enrollment,stu3.marks);	
   }
}
