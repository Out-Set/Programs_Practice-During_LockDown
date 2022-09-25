#include<stdio.h>
#include<conio.h>

void main()
{
    int i,j,k,n;
    printf("enter the no of rows");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        k=n-i;
        for(j=1;j<=n;j++)
            if(j<=(n+1)-i){
                printf("%d ",k);
                k--;}
            else
                printf(" ");
        printf("\n");
    }
}
