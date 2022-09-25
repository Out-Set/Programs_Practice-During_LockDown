#include<stdio.h>
void main()
{
  int a,b,s,fact=1,sum=0,choice;
  while(1)
  {
  clrscr();
  printf("Enter the choice\n1:addition\n2:even-odd\n3:print faccorial of n no\n4:print n no\n5:print sum of n no\n6:greatest no in b/w three no\n7:exit\n");
  scanf("%d",&choice);
   switch(choice)
   {
    case 1:
    printf("enter the two no\n");
    scanf("%d%d",&a,&b);
    s=a+b;
    printf("addition of the no is%d",s);
    break;
    case 2:
    printf("enter a no\n");
    scanf("%d",&a);
    a%2==0?printf("no is even"):printf("no is odd");
    break;
    case 3:
    printf("enter the n\n");
    scanf("%d",&b);
    for(a=1;a<=b;a++)
    {
    fact=fact*a;
     printf("\n%d",fact);
    }
    break;
    case 4:
    printf("enter the no\n");
    scanf("%d",&s);
    for(a=1;a<=s;a++);
     printf("\n%d",a);
    break;
    case 5:
    printf("enter the no\n");
    scanf("%d",&a);
    for(s=1;s<=a;s++)
    {
     sum=sum+s;
     printf("\n%d",sum);
    }
    break;
    case 6:
    printf("enter three no\n");
    scanf("%d%d%d",&a,&b,&s);
    if(a>b&&a>s)
    printf("%d is greatest",a);
    if(b>a&&b>s)
    printf("%d is greatest",b);
    if(s>a&&s>b)
    printf("%d is greatest",s);
    break;
    case 7:exit(0);
    default:
    printf("invalid choice");
  }
  getch();
  }
}