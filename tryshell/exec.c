#include <stdio.h>
#include <unistd.h>

int main()
{
	char cmd[] = "ls";
	char *argv[] = {"ls",NULL};
	char *envpv[] = {NULL};

	if(execvp(cmd, argv) == -1)
	{
		printf("Command not found\n");
	}

	return 0;
}
