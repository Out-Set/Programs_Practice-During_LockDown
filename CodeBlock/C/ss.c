int main()
{
	int i,j,n;
	printf("enter the no of rows: \n");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			if(j>=n+1-i)
			printf("%d",j+2);
			else
			printf(" ");
		}
		printf("\n"); 
	}
	return(0);
}
