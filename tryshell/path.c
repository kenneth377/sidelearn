#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main()
{
	char* envv = getenv("PATH");
	char *token;
	char *cmd = "ls";
	char *cmdl[] = {"ls", "-l",NULL};

	token = strtok(envv, ":");

	while(token!=NULL)
	{
		printf("%s\n", token);
		strcat(token, cmd);
		if(execve(token,cmdl,NULL )== -1)
		{
			printf("Error");
		}

		token = strtok(NULL,":");
	}

	printf("%s\n", envv);

	return 0;

}

