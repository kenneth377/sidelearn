#include <stdio.h>

int main()
{
	int a = 2;
	int b = 3;

	printf("a is %d\nb is %d\n\n", a, b);
	a = a+b;
	b = a-b;
	a = a-b;

	printf("a1 is %d\nb1 is %d\n\n", a, b);
	return (0);
}
		

