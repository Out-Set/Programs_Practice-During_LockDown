
void linearsearch(int n,int a[],int m);
void main()
{
    int m=12,n,x=0,j;
    int a[]={12,34,56,76,7,8,9,2,3,45,12,90};
    printf("enter the numbers you wanna search");
    scanf("%d",&n);
    linearsearch(int n,int a[],int m);

}
void linearsearch(int n,int a[],int m)
{
    int i,p=0,j=0;
    for(i=0;i<=m;i++)
    {
        if(a[i]>a[i+1])
        {
            p=a[i+1];
            a[i+1]=a[i];
            a[i]=p;
        }
    }
    for(j=0;j<=m;j++)
    {
        printf("the sorted array is: %d",a[j])
    }
}
