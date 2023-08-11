#include <stdio.h>
#include <stdlib.h>


typedef struct node *nodeptr;


struct node
{
	int data;
	nodeptr next;
};

int main()
{
	int i;
	nodeptr h;
	nodeptr new;

	i=0;
	
	nodeptr head;
	head = malloc(sizeof(struct node));

	head->data = 1;
	head->next = NULL;


	new = malloc(sizeof(struct node));

	head->next = new;

	new->data = 2;

	new->next = NULL;

	nodeptr third;

	third = malloc(sizeof(struct node));

	new->next = third;
	third->data = 3;
	third->next = NULL;

	h = head;
	while(h)
	{
		i++;
		printf("%d\n", h->data);
		h =h->next;
	}

	printf("%d\n", i);
	
	return(0);
}
