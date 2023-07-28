#include <stdio.h>


int factorial(int n)
{       
	if (n <= 0)
	{       
		return 1;
	}       

	return n * factorial( n - 1);
}               

int main()
{       
	long long ans;
	int n;

	printf("Please enter the number whose factorial you want to calculate: ");
	scanf("%d", &n);
	ans = factorial(n);
	printf("%lld\n", ans);
	
	return 0;
}
