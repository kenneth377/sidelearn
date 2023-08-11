#include "main.h"
#include <stdio.h>

int _atoi(char *s)
{
	int i;
	int sign;
	int digit;

	digit = 0;
	i = 0;
	sign = 1;
	
	while(s[i] != '\0')
	{
		if(s[i] == '-')
		{
			sign++;
		}
		else if(s[i] >= 48 && s[i] <=57)
		{
			digit  = digit * 10 + (s[i] - '0');
			if (!(s[i+1] >= 48 && s[i+1] <=57))
					break;
		}
		
		
	}

	if(sign % 2 == 1)
		sign = -1;

	return (0); 

}
