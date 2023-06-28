#include <stdio.h>


int main(void)
{
	int k=2;
	int *ptr;
	ptr = &k;

	printf("%p\n", (void *)ptr);
	printf("%d\n", *ptr);
	return (0);
}
