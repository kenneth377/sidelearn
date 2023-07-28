#include <stdio.h>

int numsum (int num)
{
	int sum;
	int n;

	sum = 0;

	while(num)
	{
		n  = num % 10;
		num = num / 10;

		sum = sum + n;
	}

	return sum;
}

int main ()
{
	int num;

	printf("Please enter the number whose digits you want to add up: ");

	scanf("%d", &num);

	printf("%d\n", numsum(num));

	return 0;
}
