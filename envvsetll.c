//This is a small program to set and read environment variables

#include <stdio.h>
#include <stdlib.h>


extern char **environ;

char *read(char *val){
    char *rval = getenv(val);
    if(rval == NULL) {
        printf("%s is not set\n", val);
    } else {
        printf("%s=%s\n", val, rval);
    }
    return rval;
}

int setter(char *attr,char *val){
	if(setenv(attr,val,1)!=0)
	{
		printf("\n setenv() failed\n");
		return 1;
	}
	printf("Environment variable successfully updated\n");
	return 0;
}


int main(int argc, char *argv[]){
	if(argc <2){
		printf("At least add one argument\n");
		return 1;
	}
	else if(argc ==2){
		read(argv[1]);
	}
	else if(argc == 3){
		setter(argv[1],argv[2]);
	}
	else{
		return 1;
	}

	return 0;
}
