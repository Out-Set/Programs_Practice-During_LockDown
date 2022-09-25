void main()
{
    int a,b;

    printf("enter the value for a: \n");
    scanf("%d",&a);

    printf("enter the value for b: \n");
    scanf("%d",&b);

    printf("before swapping the values of a=%d & b=%d\n",a,b);

    b=a+b-(a=b); // The single line code to swap.

    printf(" after swapping the values of a=%d & b=%d",a,b);

    getch();
}
