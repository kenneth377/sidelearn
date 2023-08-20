#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

extern char **environ;

int main(void)
{
	char *line = NULL;  // Pointer to hold user input
	size_t len = 0;     // Initial size for getline to allocate
	ssize_t read;       // ssize_t is the return type of getline
	int rep = 1;    // Initialize rep to 1 to start the loop
	char *token;
	char *argv[100];
	int i;
	int status;
	char *envv ;
	char *path_copy;
	char *full_path;
	pid_t child_pid;

	while (rep == 1)    // Use rep == 1 to continue looping
	{
		printf("$ ");
		read = getline(&line, &len, stdin);  // Read user input

		if (read == EOF)
		{
			free(line);
			line = NULL;
			printf("EOF (Ctrl+D) detected. Exiting.\n");
			sleep(1);
			return (0);
		}
		else if (read <= 1) {  // Check if only Enter was pressed
			continue; // Skip processing and prompt again
		}
		if (line[read - 1] == '\n')
		{
			line[read - 1] = '\0';
		}

		token = strtok(line, " \n");

		for (i = 0; token != NULL; i++)
		{
			argv[i] = token;
			token = strtok(NULL, " \n");
		}
		argv[i] = NULL;   // Set the last element of argv to NULL

		if (strcmp(argv[0], "exit") == 0)
		{
			printf("Exiting...\n");
			sleep(1);

			if (argv[1] != NULL)
			{
				status = atoi(argv[1]);
				free(line);
				line = NULL;
				exit(status);
			}
			else
			{
				exit(0);  // Exit with status code 0 if no status code provided
			}
		}

		envv = getenv("PATH");
		path_copy = strdup(envv);

		token = strtok(path_copy,":");
		
		for(i=0; token!=NULL; i++)
		{
			snprintf(full_path, sizeof(full_path), "%s/%s", token, argv[0]);
			printf("%s\n", full_path);
			free(full_path);
			token = strtok(NULL,":");
		}
		free(path_copy);

		child_pid = fork(); //creates a new child process

		if (child_pid == -1)
		{
			perror("fork");
			exit(EXIT_FAILURE);
		}
		else if (child_pid == 0)
		{
			// Child process
			// Code specific to the child process follows
			if (execve(argv[0], argv, environ) == -1)
			{
				if (execvp(argv[0], argv) == -1)
				{
					perror("./shell");
				}
			}
		}
		else
		{
			// Parent process
			// Code specific to the parent process follows
			wait(NULL); // Wait for the child process to complete
		}

		// Clear the memory allocated by getline
		free(line);
		line = NULL;
	}

	return (0);
}
