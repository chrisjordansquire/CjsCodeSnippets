#include "stdio.h"
#include "unistd.h"

// Want a fun adventure? Try to find the header file that defines
// the environ variable. Hours of fun for the whole family!

extern char **environ;

int main(){

    char ** e = environ;
    while(*e){
        printf("%s\n", *e);
        e++;
    }

}
