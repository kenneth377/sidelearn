#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *command = (char *)malloc(sizeof(char)*100);
	int i = 0;
	while(i==0)
	{
		printf("$");
		scanf("%s", command);
	}
	free(command);
	return 0;
}
