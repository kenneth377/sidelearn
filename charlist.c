#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

/*
 *This is a C programme which lists all characters and their ASCII value
 * */

int main(){
      char c;

      c = CHAR_MIN;
      while(c != CHAR_MAX){
              printf("%c:%d\n", c, c);
              c = c+1;
      }
	return (0);
}
