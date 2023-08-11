#include <stdio.h>

int cmp(char *s, char *t)
{
	if (*s != *t)
	{
		return(0);
	}
	if (*s == *t && *s != '\0')
	{
		return cmp(s+1, t+1);
	}

	return(1);
}

int main()
{
	char s[10];
	char t[10];

	printf("Please enter first string: ");

	scanf("%s", s);

	printf("Please enter second string: ");

	scanf("%s", t);

	printf("%d\n", cmp(s, t));

	return (0);
}
