#include <stdio.h>

int countstr(char *s)
{

	if(!*s)
	{
		return 0;
	}

	return countstr(s+1) + 1;
}


int main()
{
	char str[100];
	printf("Please enter the string whose length you want to count: ");

	scanf("%99s",str);

	printf("%d\n", countstr(str));

	return 0;
}
