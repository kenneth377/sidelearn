#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* next;
};

int main(){

    struct Node* head = (struct Node*)malloc(sizeof(struct Node));
    head->data=2;
    head->next =NULL;

    struct Node* first = (struct Node*)malloc(sizeof(struct Node));
    first->data=2;
    first->next =NULL;

    head->next = first;

    printf("%p",(void*)head->next);

    free(head);
    free(first);

    return 0;
}