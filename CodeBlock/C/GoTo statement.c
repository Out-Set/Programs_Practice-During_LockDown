void main()
{
    int x;
    start:
    for(x=1;x<=10;x++)
    {
        printf("%d",x);
        if(x==5)
            goto start;
        if(x==6)
            break;
    }

}
