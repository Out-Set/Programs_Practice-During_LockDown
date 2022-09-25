#include<stdlib.h>
#include<stdio.h>
int main()
{
    system("color b1");

    int *ptr;
    int n,i,sum=0;
    printf("program to calculate the sum of n no.\n");
    printf("enter the no of elements\n");
    scanf("%d",&n);
    ptr=(int *)malloc(n*sizeof(int));

    if(ptr==NULL)
    {
        printf("Memory not allocated\n");
        exit(0);
    }
    else
        printf("Memory allocated successfully\n");

    for(i=1;i<=n;i++)
    {
        printf("Enter the %d element\n",i);
        scanf("%d",ptr+i);
        sum+=*(ptr+i);
    }
    printf("Sum is: %d",sum);

    free(ptr);
    return(0);
}
