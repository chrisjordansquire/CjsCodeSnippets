//This can be built using icc and arguments from the MKL
//link line advisor. Or it can be built against the reference
//lapack simply by changing the include mkl to include lapacke.h,
//and pointing to the write header files/libraries
//
//Remember that when linking the static library for openBLAS
//you don't need to use any flags, just write something like
//gcc dgtsv_example.c -I$HOME/include $HOME/lib/libopenblas.a
#include <stdio.h>
#include "lapacke.h"

void print_arr(double* arr, int size, char* msg){
    int i;
    printf("-------------------------\n");
    printf("%s\n", msg);
    for(i=0; i<size; i++){
        printf("%g\n", arr[i]);
    }
    printf("-------------------------\n");
}

int main (int argc, const char * argv[])
{

    double dl[9];
    double d[10];
    double du[9];
    double b[10];
    lapack_int info,m,n,lda,ldb,nrhs;
    int i;
    for(i=0; i<9; i++){
        dl[i]=1;
        du[i]=1;
    }

    for(i=0; i<10; i++){
        d[i]=4;
        b[i]=i;
    }

    n = 10;
    nrhs = 1;
    ldb = 10;

    info = LAPACKE_dgtsv(LAPACK_COL_MAJOR,
            n, nrhs, dl, d, du, b, ldb);

    print_arr(b, 10, "the solution, x");
    print_arr(dl, 9, "the lower diagonal, dl");
    print_arr(d, 10, "the diagonal, d");
    print_arr(du, 9, "the upper diagonal, du");

    printf("info: %d\n", info);

    return(info);
}
