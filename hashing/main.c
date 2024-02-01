#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 10

typedef struct Nati {
    char *value;
    char *key;
} node;

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
        return 0;
    }
    HASHTABLE[hashval] = k;
    return 1;
}

int main() {
    node* newn = (node *)malloc(sizeof(node));
    newn->value = "Appiah";
    newn->key = "name";

    printf("%s\n", newn->value);
    printf("%d\n", hashfunc(newn->value));

    // Initialize HASHTABLE with NULL pointers
    for (int i = 0; i < TABLE_SIZE; i++) {
        HASHTABLE[i] = NULL;
    }

    // Initialize hash table with new node
    int result = hashinit(newn);
    if (result == 1) {
        printf("Node inserted successfully into hash table.\n");
    } else {
        printf("Collision occurred. Node not inserted into hash table.\n");
    }

    free(newn); // Don't forget to free dynamically allocated memory
    return 0;
}
