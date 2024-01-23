#include "monty.h"
#include <string.h>

void push(stack_t **stack, unsigned int line_number);
void pall(stack_t **stack, unsigned int line_number);
void pint(stack_t **stack, unsigned int line_number);

int main(int argc, char *argv[]) {
    char s[100];
    if (argc != 2) {
        perror("USAGE: monty file");
        exit(EXIT_FAILURE);
    }
    stack_t* head = (stack_t*)malloc(sizeof(stack_t));
    head->prev = NULL;
    head->next = NULL;
    head->n = (int)NULL;

    stack_t* first = (stack_t* )&head;

    FILE* fp;

    fp = fopen(argv[1], "r");
    if (fp == NULL) {
        fprintf(stderr, "Error: Can't open file %s", argv[1]);
        exit(EXIT_FAILURE);
    }
    int linenumber = 1;
    while (fgets(s, 100, fp) != NULL) {
        if (s[0] == '#' || s[0] == '\n') {
            continue;
        }
        char *token = strtok(s, " ");
        while (token != NULL) {
            if (strcmp(token, "push") == 0) {
                push(&head,linenumber);
            }
            else if (strcmp(token, "pall") == 0) {
                pall(&head,linenumber);
            }
            else if (strcmp(token, "pint") == 0) {
                pint(&first,linenumber);
            }
            else{
                // token = strtok(NULL, " ");
                break;
            }
            // printf("L%d:%s\n", linenumber, token);
            token = strtok(NULL, " ");
        }
        linenumber++;
    }

    fclose(fp);
    free(head);

    return 0;
}
