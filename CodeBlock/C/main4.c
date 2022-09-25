#include <stdio.h>
struct profile
{
	char name[20],f[20];
	int mob;
};
void main()
{
	struct profile f1,f2={"ram","shyam",9087654567};
	f1.mob=8795424016;
	strcpy(f1.f="rajesh");
	printf("enter the name of student");
	scanf("%s",&f1.name);
	printf("%s\t%s\t%d",f1.name,f1.f,f1.mob);
	printf("%s\t%s\t%d",f2.name,f2.f,f2.mob);
}
