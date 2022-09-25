void main()
{
    int n,m;
    char c,d;
    printf("Please first make your username and pass \n");
    printf("choose a username containing only character: ");
    scanf("c",&c);
    printf("write your password containing only integers:  ");
    scanf("d",&n);

    printf("login form\n");
    printf("Please enter your username and pass \n");
    printf("enter your username: ");
    scanf("c",&d);
    printf("enter your password:  ");
    scanf("d",&m);
    if(d==c&&m==n)
    {
        printf("login successful");
    }
    else if(d!=c)
        printf("invalid username\n");
    else if(m!=n)
        printf("invalid password\n");
    else
        printf("invalid username & password\n");

}
