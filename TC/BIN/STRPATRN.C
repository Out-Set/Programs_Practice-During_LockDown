main()
{
 int i,j,n,s;
 clrscr();
 printf("enter the no of rows\n");
 scanf("%d",&n);
 for(i=0;i<=n;i++)
  {
  for(s=1;s<=n;s++)
   {
    printf(" ");
   }
    n--;

    for(j=0;j<=i;j++)
     {
      printf("%d",i);
     }
    printf("\n");
  }
 getch();
 return(0);
}