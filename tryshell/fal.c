#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

extern char **environ;

int main() {
	char *line = NULL;  // Pointer to hold user input
	size_t len = 0;     // Initial size for getline to allocate
	ssize_t read;       // ssize_t is the return type of getline
	int rep = 1;    // Initialize rep to 1 to start the loop
	char *token;
	char *argv[100];
	int i, j;
	char cmd[] = "/usr/bin/";
	pid_t child_pid;

	while (rep == 1)    // Use rep == 1 to continue looping
	{
		printf("$ ");
		read = getline(&line, &len, stdin);  // Read user input

		if (read == EOF) {
			free(line);
			line = NULL;
			printf("EOF (Ctrl+D) detected. Exiting.\n");
			return 0;
		} else if (read == -1) {
			printf("getline error\n");
			continue;
		}

		// Process and handle the user input

		token = strtok(line, " \n");

		for (i = 0; token != NULL; i++)
		{
			argv[i] = token;
			token = strtok(NULL, " \n");
		}
		argv[i] = NULL;   // Set the last element to NULL

		if(argv[0]=="exit")
		{
			free(line);
			line = NULL;
			return 0;
		}
		// Concatenate cmd and token
		strcpy(cmd, "/usr/bin/"); // Reset cmd
		strcat(cmd, argv[0]);

		child_pid = fork();

		if (child_pid == -1) {
			perror("fork");
			exit(EXIT_FAILURE);
		}
		else if (child_pid == 0) {
			// Child process
			// Code specific to the child process goes here
			if (execve(cmd, argv, environ) == -1) {
				strcpy(cmd, "/usr"); // Reset cmd
				strcat(cmd, argv[0]);
				if(execve(cmd, argv, environ) == -1)
				{
					if(execve(argv[0], argv, environ) == -1)
					{
						perror("./shell");
					}
				}
			}
		}
		else {
			// Parent process
			// Code specific to the parent process goes here
			wait(NULL); // Wait for the child process to complete
		}

		// Clear the memory allocated by getline
		free(line);
		line = NULL;
	}

	return 0;
}

