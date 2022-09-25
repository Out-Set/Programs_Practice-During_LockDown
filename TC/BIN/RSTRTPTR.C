int length(char *);
char* reverse(char *);
main()
{
 clrscr();
 printf("%d",length("computer"));
 printf("\n%u",reverse("computer"));
 getch();
}
char* reverse(char *p)
{
 int i,l;
 char t;
 for(i=0;*(p+i)!='\0';i++)
 {
  for(i=0;i<l/2;i++)
  {
   t=*(p+i);
   *(p+i)=*(p+l-1-i);
   *(p+l-1-i)=t;
  }
 }
 return(p);
}
int length(char *p)
{
 int i;
 for(i=0;*(p+i)!='\0';i++)
 return(i);
}