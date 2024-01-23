#include "monty.h"
#include <string.h>

void push(stack_t **stack, unsigned int line_number)
{
    char *token = strtok(NULL, " ");
    if (token == NULL)
    {
        fprintf(stderr, "L%d: usage: push integer\n", line_number);
        exit(EXIT_FAILURE);
    }

    stack_t *newnode = (stack_t *)malloc(sizeof(stack_t));
    if (newnode == NULL)
    {
        perror("Error: malloc failed");
        exit(EXIT_FAILURE);
    }

    newnode->n = atoi(token);

    if (*stack == NULL)
    {
        newnode->prev = NULL;
        newnode->next = NULL;
        *stack = newnode;
    }
    else
    {

        newnode->prev = NULL;
        newnode->next = *stack;
        (*stack)->prev = newnode;
        *stack = newnode;
        printf("%p : %d\n",newnode, newnode->n);
    }
}
