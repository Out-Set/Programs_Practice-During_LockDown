main()
{
    int a[]={12,34,56,76,7,8,9,2,3,45,12,90};
    int i=0,b,m=11;
    int flag=0;
    printf("12,34,56,76,7,8,9,2,3,45,12,90\n");
    printf("enter the no you wanna search:\n ");
    scanf("%d",&b);

    for(i=0;i<=m;i++)
    {
        if(a[i]=b)
            flag=1;
    }
    if(flag=1)
        printf("found\n");

    printf("not found");

    getch();
}
