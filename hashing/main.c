#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 10

typedef struct Node node;

struct Node {
    char *value;
    char *key;
    node *next; 
};

node *HASHTABLE[TABLE_SIZE];

unsigned int hashfunc(char *s) {
    unsigned int hashval = 0;
    size_t length = strlen(s);

    for (size_t i = 0; i < length; i++) {
        hashval += s[i];
    }

    return hashval % TABLE_SIZE;
}

int hashinit(node *k) {
    int hashval = hashfunc(k->key);
    
    if (HASHTABLE[hashval] != NULL) {
        k->next = HASHTABLE[hashval];
    }

    HASHTABLE[hashval] = k; 
    return 1; 
}

void printhash(node **HASHTABLE) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        node *current = HASHTABLE[i];
        printf("Index %d:", i);
        while (current != NULL) {
            printf(" (%s, %s)", current->key, current->value);
            current = current->next;
        }
        printf("\n");
    }
}


int key_index(char *key) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        node *current = HASHTABLE[i];
        while (current != NULL) {
            if (strcmp(current->key, key) == 0) {
                return i;
            }
            current = current->next;
        }
    }
    return -1; 
}

char *hashvalget(char *key) {
    // for (int i = 0; i < TABLE_SIZE; i++) {
    //     node *current = HASHTABLE[i];
    //     while (current != NULL) {
    //         if (strcmp(current->key, key) == 0) {
    //             return current->value;
    //         }
    //         current = current->next;
    //     }
    // }
    // return "Key not found";

   if (key == NULL) {
        return "Key cannot be NULL";
    }

    int keyval = hashfunc(key);
    if (HASHTABLE[keyval] != NULL) {
        if (strcmp(HASHTABLE[keyval]->key, key) == 0) {
            return HASHTABLE[keyval]->value;
        }

        node *current = HASHTABLE[keyval]->next;
        while (current != NULL) {
            if (strcmp(current->key, key) == 0) {
                return current->value;
            }
            current = current->next;
        }
    }
    
    return "Key not found";
}


int main() {
    node* newn = (node *)malloc(sizeof(node));
    newn->value = "Appiah";
    newn->key = "name";
    newn->next = NULL;

    node* newn2 = (node *)malloc(sizeof(node));
    newn2->value = "Asokwa";
    newn2->key = "hometown";
    newn2->next = NULL;

    for (int i = 0; i < TABLE_SIZE; i++) {
        HASHTABLE[i] = NULL;
    }

    int result = hashinit(newn);
    if (result == 1) {
        printf("Node inserted successfully into hash table.\n");
    } else {
        printf("Failed to insert node into hash table.\n");
    }

    result = hashinit(newn2);
    if (result == 1) {
        printf("Node inserted successfully into hash table.\n");
    } else {
        printf("Failed to insert node into hash table.\n");
    }

    char* tt =hashvalget("name");

    printf("%s\n",tt);
    int rr = key_index("name");
    printf("%d\n",rr);
    printhash(HASHTABLE);
    
    free(newn);
    free(newn2);

    return 0;
}