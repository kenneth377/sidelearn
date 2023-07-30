#include <stdio.h>

int sqrti(int num, int i)
{
	if(num<0)
	{
		return -1;
	}
	else if (num == 1)
	{
		return 1;
	}
	else if (i > num/2)
	{
		return -1;
	}
	else if (i*i == num)
	{
		return(i);
	}
	else
	{
		return sqrti(num,i+1);
	}
}

int main ()
{
	int num;
	int i;

	i=0;

	printf("Please enter the number whose square root you want to find: ");

	scanf("%d",&num);

	printf("%d\n", sqrti(num,i));

	return 0;
}
