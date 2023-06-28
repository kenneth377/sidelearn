#include "main.h"
#include <string.h>
#include <stdio.h>

void rev_string(char *s)
{
	int i;
	int len = strlen(s) - 1;
	

	for (i = 0; i < len/2; i++)
	{
		 printf("%c %c\n", s[i], s[len - i]);
		printf("%i %i\n", i, len-i);
		 s[i] = s[i]+s[len-i];
		s[len - i] = s[i] - s[len -i];
		s[i] = s[i]- s[len - i];
/*		temp = s[i];
		s[i] = s[len - i];
		s[len - i] = temp;
*/
		printf("%c %c\n", s[i], s[len - i]);

/*		s[i] = s[i] + s[len - i];
		s[len - i] = s[i] - s[len - i];
		s[i] = s[i] - s[len - i];
*/	}
}
