#include<stdio.h>
void main()
{
 int year,period;
 float ammount,inrate,value;
 printf("input ammount,interest rate & period\n");
 scanf("%f%f%d",&ammount,&inrate,&period);
 printf("/n");
 year=1;

 while(year<=period)
  {
   value=value+inrate*ammount;
   printf("2%d rs 8.2%f\n",year,value);
   ammount=value;
   year=year+1;
  }
 getch();;
}