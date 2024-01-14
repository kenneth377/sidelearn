#include <stdio.h>
#include <stdlib.h>


int main(){
    FILE* fp;
    fp =fopen("file.txt","w");

    fprintf(fp,"%s\n","Hard as usual");
    fprintf(fp,"%s","No yawa, we move");
    fclose(fp);


    return 0;
}