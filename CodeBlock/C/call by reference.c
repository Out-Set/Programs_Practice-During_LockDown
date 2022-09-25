#include<stdio.h>
#include<conio.h>
void swap(int *,int *);
void main()
{
    int a,b;
    printf("enter two no\n");
    scanf("%d%d",&a,&b);
    printf("the values of a & b before swapping is: %d & %d\n",a,b);
    swap(&a,&b);
}
void swap(int *x,int *y)
{
    int temp;
    temp=*x;
    *x=*y;
    *y=temp;
    printf("the values of a & b after swapping is: %d & %d",*x,*y);
}
