main()
{
    int *ptr;
    int n,sum=0;
    printf("Program to print Sum of n no\n");
    printf("Enter the no up to you wanna calculate Sum\n");
    scanf("%d",&n);

    ptr=(int *)malloc(sizeof(int));

    for(int i=0;i<=n;i++)
    {
      printf("Enter the no");
      scanf("%d",ptr+i);
      sum+=*(ptr+i);
    }
    printf("%d",sum);
}
