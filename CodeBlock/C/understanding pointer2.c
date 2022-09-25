main()
{
    int a=8;
    int *b,**c,***d,****e,*****f;
    b=&a;
    c=&b;
    d=&c;
    e=&d;
    printf("The value of a is: %d\n",a);
    printf("address of a is: %d\n",b);

    printf("The value of b is: %d\n",b);
    printf("address of b is: %d\n",c);

    printf("The value of c is: %d\n",c);
    printf("address of c is: %d\n",d);

    printf("The value of d is: %d\n",d);
    printf("address of d is: %d\n",e);

    printf("The value of e is: %d\n",e);

}
