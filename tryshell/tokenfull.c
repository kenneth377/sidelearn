#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
	char *av[100];
	char *token;
	char *line = NULL;
	size_t len;
	ssize_t reader;
	int i;

	printf("$ ");
	reader =  getline(&line, &len, stdin);

	token = strtok(line, " ");
	
	for(i=0; token!= NULL; i++)
	{
		printf("%s\n",token);
		av[i] = token;

		token = strtok(NULL, " ");
	}
	av[i] = NULL;
	i= 0;

	while(av[i])
	{
		printf("%s\n", av[i]);
		i++;
	}

	free(line);

	return 0;
}
