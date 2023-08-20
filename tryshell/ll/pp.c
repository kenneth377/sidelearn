#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

extern char **environ;

int main(void) {
	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	int rep = 1;
	char *token;
	char *argv[100];
	int i;
	int status;
	char *envv;
	char *path_copy;
	char full_path[256];
	pid_t child_pid;

	while (rep == 1) {
		printf("$ ");
		read = getline(&line, &len, stdin);

		if (read == EOF) {
			free(line);
			line = NULL;
			printf("EOF (Ctrl+D) detected. Exiting.\n");
			sleep(1);
			return (0);
		} else if (read <= 1) {
			continue;
		}
		if (line[read - 1] == '\n') {
			line[read - 1] = '\0';
		}

		token = strtok(line, " \n");

		for (i = 0; token != NULL; i++) {
			argv[i] = token;
			token = strtok(NULL, " \n");
		}
		argv[i] = NULL;

		if (strcmp(argv[0], "exit") == 0) {
			printf("Exiting...\n");
			sleep(1);

			if (argv[1] != NULL) {
				status = atoi(argv[1]);
				free(line);
				line = NULL;
				exit(status);
			} else {
				exit(0);
			}
		}

		envv = getenv("PATH");
		path_copy = strdup(envv);

		token = strtok(path_copy, ":");

		while (token != NULL) {
			snprintf(full_path, sizeof(full_path), "%s/%s", token, argv[0]);
			printf("%s\n", full_path);

			if (access(full_path, X_OK) == 0) {
				child_pid = fork();

				if (child_pid == -1) {
					perror("fork");
					exit(EXIT_FAILURE);
				} else if (child_pid == 0) {
					// Child process
					if (execve(full_path, argv, environ) == -1) {
						if (execvp(full_path, argv) == -1) {
							perror("./shell");
						}
					}
				} else {
					// Parent process
					wait(NULL);
				}
				break;  // Command executed or not, exit the loop
			}

			token = strtok(NULL, ":");
		}

		free(path_copy);
		free(line);
		line = NULL;
	}

	return (0);
}
