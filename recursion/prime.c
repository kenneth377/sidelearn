#include <stdio.h>

int primi(int num, int i)
{
	if (num==0 || num == 2)
	{
		return (1);
	}
	else if (num <= 1 )
	{
		return (0);
	}
	else if  (num % i == 0)
	{
		return (0);
	}
	else if (i > num / 2)
	{
		return (1);
	}
	else
	{
		return primi(num, i+1);
	}
}

int main()
{
	int num;
	int i;

	i = 2;
	printf("Please enter the number to check wheter it is prime or not: ");

	scanf("%d", &num);

	printf("%d\n", primi(num, i));

	return 0;
}
