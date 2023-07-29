#include <stdio.h>

int powi (int x, int y)
{
	if (x<0)
	{
		x = -x;
		if(y>0)
                {
                        return -x * powi(x,y-1);
                }
		return -1;
	}

	else
	{
		if(y>0)
		{
			return x * powi(x,y-1);
		}
		return 1;
	}
}
int main()
{
	int x;
	int y;
	printf("Please enter the base: ");

	scanf("%d", &x);

	printf("Please enter power: ");

	scanf("%d", &y);

	printf("%d\n", powi(x, y));

	return 0;
}
