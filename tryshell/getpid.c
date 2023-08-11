#include <stdio.h>
#include  <unistd.h>


int main()
{
	pid_t my_pid;
	pid_t child_pid;

	my_pid = getpid();
	child_pid = fork();

	printf("%u\nChild: %u\nParent: %u\n", my_pid, child_pid, getppid());

	return 0;
}
