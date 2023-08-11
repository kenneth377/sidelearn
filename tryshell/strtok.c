#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	char *token;


	printf("$ ");

	read = getline(&line, &len, stdin);

	if(read == -1)
	{
		printf("failed");
		return -1;
	}
	else
	{
		token = strtok(line, " ");
		while(token != NULL)
		{
			printf("%s\n", token);
			token = strtok(NULL, " ");
		}
	}

	return 0;
}
