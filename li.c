/* Hard as usual. We move
Simple implementation of a singly linked-lists with addition and roemoval functions*/
#include <stdio.h>


struct Node* addnodeatbeginning(struct Node* h, struct Node* n);
struct Node* addnodeaftertindex(struct Node* h, struct Node* n, int index);
struct Node* addnodeatend(struct Node* h, struct Node* n);

struct Node* removeatbeginning(struct Node* h);
struct Node* removeaindex(struct Node* h, int index);
struct Node* removeatend(struct Node* h);

void printlist(struct Node* h);
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
   
    printlist(hi);

    hi = removeatbeginning(hi);
    printlist(hi);

    hi = removeatend(hi);
    printlist(hi);

        return 0;

}


void printlist(struct Node* hi){
    if(hi){
        while(hi){
            printf("%d\n",hi->data);
            hi = hi->next;   
        }
    }
    else{
        printf("List is empty\n");
        return;
    }
}

struct Node* addnodeatend(struct Node* h, struct Node* n){
     if(!h){
        return NULL;
    }
    struct Node* cu = h;

    while(cu->next){
        cu = cu->next;
    }

    cu->next = n;

    return h;
}

struct Node* addnodeatbeginning(struct Node* h, struct Node* n){
    if(h){

        n->next = h;
    }

    return n;
}

struct Node* addnodeaftertindex(struct Node* h, struct Node* n, int index){
    struct Node* startnode =h; 
     if(!h||!n||!index){
        return NULL;
    }
    int cuindex = 0;

    while(cuindex < index){
        if(h->next){
            h =h->next;
            cuindex += 1;
        }
        else{
            printf("Index Error: Index does not exist in linked list\n");
            return NULL;
        }
    }
    struct Node* nodenext =h->next;
    h->next = n;
    n->next = nodenext;

    return startnode;
}


struct Node* removeatbeginning(struct Node* h){
     if(!h){
        return NULL;
    }

    struct Node* newhead = h->next;

    h->next = NULL;
    
    return  newhead;
}


struct Node* removeatend(struct Node* h){
    if(!h){
        return NULL;
    }
    else if(!h->next){
        return NULL;
    }
    struct Node* cu = h;
    while(cu->next->next){
        cu= cu->next;
    }
    cu->next =NULL;
    return h;
}

struct Node* removeafterindex(struct Node* h, int index){
    struct Node* startnode =h;
    if(!h||!index){
        return NULL;
    }
    int cu =0;

    while(cu< index){
        if(h->next){
            h=h->next;
            cu+=1; 
        }
        else{
            printf("Index Error:Index does not exist in linked list ");
            return NULL;
        }  
    }

    h->next =NULL;
    return startnode;
}