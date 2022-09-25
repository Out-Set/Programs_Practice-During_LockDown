void input(int *p);
void disp(int *p);
void sort(int *p);
void main()
{
 int a[5];
 clrscr();
 input(a);
 disp(a);
 sort(a);
 disp(a);
 getch();
}
void input(int *p)
{
 int i;
 printf("enter five no\n");
 for(i=0;i<5;i++)
  scanf("%d",p+i);
}
void disp(int *p)
{
 int j;
 for(j=0;j<5;j++)
  printf("%d\t",*(p+j));
 printf("\n");
}
void sort(int *p)
{
 int i,j,t;
 for(j=1;j<5;j++)
 {
  for(i=0;i<4-j;i++)
  {
   if(*(p+i)>*(p+i+1))
   {
    t=*(p+i);
    *(p+i)=*(p+i+1);
    *(p+i+1)=t;
   }
  }
 }
}