void main()
{
    int a=5,b=9;
    int *p,*q;
    p=&a,q=&b;
    printf("%d\n%d",a,b);//value of a and b
    printf("%d\n%d\n",p,q);//address of p and q
    printf("%d\n%d",*p,*q);//value at particular address
}
