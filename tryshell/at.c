#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int *argc, char *argv[])
{
	char line[] = "exit 98";
	int num ;
	char *token;
/*	char *argv[100];
	int i;
                token = strtok(line, " \n");

                for (i = 0; token != NULL; i++)
                {
                        argv[i] = token;
                        token = strtok(NULL, " \n");
                }
              argv[i] = NULL; 
*/
	printf("%s\n",argv[0]);

	num = atoi(argv[1]);

	printf("%d\n", num);

	return 0;
}
