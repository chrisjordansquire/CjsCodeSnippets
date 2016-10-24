#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "cblas.h"

//This is compiled with the following command, assuming libopenblas
//was installed in $HOME
//gcc daxpy_ex.c -I$HOME/include $HOME/lib/libopenblas.a -std=c99 -lpthread

void print_arr(double* arr, int size, char* msg){
    int i;
    printf("-------------------------\n");
    printf("%s\n", msg);
    for(i=0; i<size; i++){
        printf("%g\n", arr[i]);
    }
    printf("-------------------------\n");
}


int main(int argc, const char** argv){

    if(argc != 4){
        printf("Usage:\n"
                "./a.out n alpha inc\n"
                "n = size of vectors\n"
                "alpha = scalar in daxpy\n"
                "inc = increment between values for daxpy\n"
                "prints x, y, and y <- alpha * x + y\n");
        exit(0);
    }

    double *x;
    double *y;
    int n = atoi(argv[1]);
    double alpha = atof(argv[2]);
    int incx = atoi(argv[3]);
    int incy = incx;


    x = malloc(sizeof(double) * n);
    y = malloc(sizeof(double) * n);

    for(int i=0; i<n; i++){
        x[i] = i+1;
        y[i] = 2*i+1;
    }

    print_arr(x, n, "x=");
    print_arr(y, n, "y=");

    cblas_daxpy(n, alpha, x, incx, y, incy);

    print_arr(y, n, "y=");

    return(0);
}


