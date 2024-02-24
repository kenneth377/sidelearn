//Simple Program to Access and list all environment variables


#include <stdio.h>

extern char **environ;
int main(int argc , char *argv[]){

	int count = 0;

	while(environ[count]){
		printf("%d: %s\n", count, environ[count]);
		count++;
	}
	return 0;
}
