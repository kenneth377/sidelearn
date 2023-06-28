#include <stdio.h>


int main(void)
{
	/*
	int i=1;
	int j;


	while(i<=5)
	{
		j=i;
		char str = '*';
		while(j>=1)
		{
			printf("%c", str);
			j--;
		}
		putchar('\n');
		i++;
	}

	*/

	int i = 5;
	int j;

	while (i>=1)
	{
		j=i;
		char str = '*';

		for (j=1; j<=i; j++)
		{
			putchar(str);
		}
		putchar('\n');
		i--;
	}

	return (0);
}
