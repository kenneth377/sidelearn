// Hard as usual. We move

#include <stdio.h>


struct Node* addnodeatbeginning(struct Node* h, struct Node* n);
void addnodeaftertindex(struct Node* h, struct Node* n, int index);
struct Node* addnodeatend(struct Node* h, struct Node* n);
struct Node{
    struct Node* next;
    int data;
};


int main(){
    struct Node head;
    head.next = NULL;
    head.data = 1;

    struct Node second;
    second.data =2;
    second.next = NULL;

    addnodeatend(&head, &second);
    
    struct Node third;
    third.data =3;
    third.next = NULL;

    struct Node atbeginning;
    atbeginning.data = -1;
    atbeginning.next = NULL;

    addnodeatend(&head,&third);

    struct Node atindex;
    atindex.data =25;
    atindex.next = NULL;

    addnodeaftertindex(&head, &atindex, 0);

    struct Node* hi = addnodeatbeginning(&head, &atbeginning);
    while(hi){
        printf("%d\n",hi->data);
        hi = hi->next;   
    }


    return 0;

}


struct Node* addnodeatend(struct Node* h, struct Node* n){
    struct Node* cu = h;

    while(cu->next){
        cu = cu->next;
    }

    cu->next = n;

    return h;
}

struct Node* addnodeatbeginning(struct Node* h, struct Node* n){
    if(h){
        // struct Node* nextnode = h->next
        n->next = h;
    }

    return n;
}

void addnodeaftertindex(struct Node* h, struct Node* n, int index){
    int cuindex = 0;

    while(cuindex < index){
        if(h->next){
            h =h->next;
            cuindex += 1;
        }
        else{
            printf("Index Error: Index does not exist in linked list\n");
            return;
        }
    }
    struct Node* nodenext =h->next;
    h->next = n;
    n->next = nodenext;

    return;
}