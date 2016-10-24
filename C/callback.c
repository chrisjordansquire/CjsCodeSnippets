#include <stdlib.h>
#include <stdio.h>

// Trivial example playing with a callback in C

void cback(int i, int j);
void trivial(int i,void (*f)(int, int));

int main(int argc, char* argv[]){

    int k = atoi(argv[1]);
    printf("%d\n\n", k);

    trivial(k, &cback);
    
}

void cback(int i, int j){

    printf("%d %d\n", i, j);

}

void trivial(int i, void (*f)(int, int)){
    
    int k;
    for(k=0; k<i; k++){
        printf("%d ", k);
        f(k*k, k*k*k);
    }

}
