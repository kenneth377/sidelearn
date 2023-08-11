#include "main.h"


char *_strcpy(char *dest, char *src)
{
	int i;

	while(src[i])
	{
		dest[i]=src[i];
		i++;
	}

	return (dest);
}
