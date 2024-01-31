#include <stdio.h>
#include <stdlib.h>


int main(){
    FILE* fp;
    fp =fopen("file.txt", "r");
    char s;
    // fprintf(fp,"%s\n","Hard as usual");
    // fprintf(fp,"%s","No yawa, we move");
    fgetc(s,fp);
    printf("%s\n",s);
    // printf("hwelo");
    fclose(fp);


    return 0;
}