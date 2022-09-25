int main()
{
    int arr[]={1,2,3,4,5};
    int *p=arr;

    ++*p;//no increment
    --*p;//no decrement

    *++p;//pre increment
    *--p;//pre decrement

    *p++;//post increment
    *p--;//post decrement

    p+=2;
    printf("%d",*p);
    return 0;
}
