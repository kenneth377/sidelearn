// // #include <stdio.h>



// // int main()
// // {

// //     typedef struct Node* Nodeptr;
// //     struct Node
// //     {
// //     Nodeptr prev;
// //     Nodeptr next;
// //     int data;
// //     };

// //     struct Node head;
// //     struct Node first;
// //     head.next = (Nodeptr)&first;

// //     struct Node second;
// //     first.next = (Nodeptr)&second;
// //     first.data = 4;
// //     second.data = 5;
// //     first.prev = (Nodeptr)&head;
// //     second.prev = (Nodeptr)&first;

// //     Nodeptr h;
// //     h = head.next;
// //     while(h){
// //         if(h->data==4){
// //             h->prev->next =h->next;
// //             h->next->prev = h->prev;
// //         }
// //         printf("%d\n", h->data);
// //         h = h->next;
// //     }
// //     // printf("%d\n",first.data);
// //     // printf("%d\n",second.data);



// //     return 0;
// // }



// // #include <stdio.h>

// // struct Node *h;
// // struct Node *n;
// // struct Node* addnode(struct Node* h, struct Node* n);

// // int main()
// // {
    
// //     struct Node{
// //         struct Node* next;
// //         char data;
// //     };

// //     struct Node head;
// //     head.data = 'A';
// //     head.next = NULL;

// //     struct Node first;
// //     head.next = &first;
// //     first.data = 'B';
// //     first.next = NULL;

// //     // struct Node second;
// //     // second.data = 'C';
// //     // second.next = NULL;

// //     // struct Node* p;
// //     // p = &head;

// //     addnode((struct Node*)&head,(struct Node*)&first)
    

// //     struct Node *h = &head;
// //     while(h){
// //         printf("%p\t %c\t %p\n",h,h->data,h->next);
// //         h = h->next; 

// //     }

// //     // printf("%p",head.next);
// //     return 0;
// // }



// // struct Node* addnode( struct Node *h,struct Node *n){
// //         struct Node* cu = h;
// //         while(cu){
// //             if(!cu->next){
// //                 cu->next = n;
// //             }
// //             cu = cu->next;           
// //         }

// //         return h;
// //     };
// // #include <stdio.h>

// // struct Node {
// //     struct Node* next;
// //     char data;
// // };

// // struct Node* addnode(struct Node* h, struct Node* n);

// // int main() {
// //     struct Node head;
// //     head.data = 'A';
// //     head.next = NULL;

// //     struct Node first;
// //     first.data = 'B';
// //     first.next = NULL;

// //     // Call the addnode function and update the head
// //     struct Node* h = addnode(&head, &first);

// //     // Print the nodes
// //     struct Node* currentNode = h;
// //     while (currentNode) {
// //         printf("%p\t %c\t %p\n", currentNode, currentNode->data, currentNode->next);
// //         currentNode = currentNode->next;
// //     }

// //     return 0;
// // }

// // struct Node* addnode(struct Node* h, struct Node* n) {
// //     struct Node* cu = h;
// //     while (cu->next) {
// //         cu = cu->next;
// //     }

// //     cu->next = n;
// //     return h;
// // }



// #include <stdio.h>


// struct Node{
//     struct Node* next;
//     struct Node* prev;
//     int data;
// };
// struct Node* addnode(struct Node* h,struct Node*n);

// int main(){

//     struct Node head;
//     head.data = 1;
//     head.next =NULL;

//     struct Node first;
//     first.data = 2;
//     first.next =NULL;

//     // struct Node* hi =addnode(NULL,&head);
//     struct Node* ho=addnode(&head,&first);
//     printf("%p\n",ho);

//     struct Node* hi = &head;
//     while(hi){
//         struct Node* nextnode =hi->next;
//         printf("%d\n",hi->data);
//         hi=nextnode;
//     }
//     return 0;
// }

// // struct Node* addnode(struct Node* h,struct Node*n){
// //     struct Node* cu = h;

// //     while(cu){
// //         if(!cu->next){
// //             cu->next =n;
// //         }
// //         cu = cu->next;
// //     }

// //     return h;
// // }

// struct Node* addnode(struct Node* h, struct Node* n) {
// struct Node* cu = h;  while (cu->next) {
//         cu = cu->next;
//     }

//     cu->next = n;
//     return h;
// }
