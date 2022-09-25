main()
{
    int a;
    printf("enter a no: \n");
    scanf("%d",&a);
    printf("the entered no  is: %d\n",a);
    printf("address of the no is: %d\n",&a);
    printf("the entered no  is: %d\n",*&a);
}
