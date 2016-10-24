#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <omp.h>

// Pretty sure this code comes from a course example from years ago, but
// I can't seem to dig it up.

typedef struct {
    double *A;
    double *B;
    double *C;
    int n;
    int bs; //block size
} dgemm_info;

//This is for multiplying C = A * B where A is 
//p by q and B is q by r
typedef void (*dgemm_impl)(dgemm_info*);

void clear_C(dgemm_info *info){
    memset(info->C, 0, info->n * info->n);
}

int time_dgemm(dgemm_impl f, dgemm_info *info,
        char* message){
    clock_t start;
    double diff;
   
    printf("%s\n", message);
    clear_C(info);
    start = clock();
    f(info);
    
    diff = (clock() - start) / (double) CLOCKS_PER_SEC;

    printf("This operation took %g sec.\n", diff);
}

double randDouble(){
    return ((double) rand() / (double) RAND_MAX);
}

void create_col_mat(dgemm_info *info){
    int n = info->n;

    info->A = malloc(sizeof(double) * n*n);
    info->B = malloc(sizeof(double) * n*n);
    info->C = malloc(sizeof(double) * n*n);

    srand(1000);
    int i;

    for(i=0; i<n*n; i++){
        info->A[i] = randDouble();
    }

    for(i=0; i<n*n; i++){
        info->B[i] = randDouble();
    }

}


void free_mat(dgemm_info *info){
    
    free(info->A);
    free(info->B);
    free(info->C);
}


void dgemm_naive(dgemm_info *info){
    int i,j,k;
    int n = info->n;
    int bs = info->bs;

    for(i=0; i<bs; i++){
        for(j=0; j<bs; j++){
            for(k=0; k<bs; k++){
                info->C[i*n+j] += info->A[i*n+k] * info->B[k*n+j];
            }
        }
    }

}

void dgemm_blocked(dgemm_info *info){
    int i,j,k;
    int n = info->n;
    int bs = info->bs;

    dgemm_info block_info;
    block_info.n = n;
    block_info.bs = bs;

    for(i=0; i<n; i+= bs){
        for(j=0; j<n; j+= bs){
            block_info.C = &(info->C[i*n + j]);
            for(k=0; k<n; k+= bs){
                block_info.A = &(info->A[i*n+k]);
                block_info.B = &(info->B[k*n + j]);
                dgemm_naive(&block_info);
            }
        }
    }
            

}

void dgemm_transposed(dgemm_info *info){
    int i,j,k;
    int n = info->n;
    
    double* tmp = (double*) malloc(sizeof(double)*n*n);

    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            tmp[i*n+j] = info->B[i+j*n];
        }
    }

    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            for(k=0; k<n; k++){
                info->C[i*n+j] += 
                    info->A[i*n+k] * tmp[j*n+k];
            }
        }
    }

    free(tmp);

}

void dgemm_omp(dgemm_info *info){

    int n = info->n;
    int bs = info->bs;
    int i, j, k;
    
    #pragma omp parallel for 
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            double sum=0;
            for(k=0; k<n; k++){
                sum += info->A[i*n+k] * info->B[k*n+j];
            }
            info->C[i*n+j] = sum;
        }
    }

}

void print_mat(double* mat, int n, char* name){
    int i, j;
    printf("%s=\n", name);
    printf("[ ");
    for(i=0; i<n; i++){
        printf("[ ");
        for(j=0; j<n; j++){
            printf("%g", mat[i*n+j]);
            if(j<(n-1)){
                printf(", ");
            }
        }
        printf("]");
        if(i<(n-1)){
            printf(",\n");
        }
    }
    printf("]\n");
}


void run_timings(dgemm_info *info, int bs){
 
    time_dgemm(&dgemm_naive, info, "dgemm_naive");
    info->bs = bs;
    time_dgemm(&dgemm_blocked, info, "dgemm_blocked");
    time_dgemm(&dgemm_transposed, info, "dgemm_transposed");
    time_dgemm(&dgemm_omp, info, "dgemm_omp");
}

void test_dgemm(dgemm_impl f, dgemm_info* info){
    int n = info->n;

    print_mat(info->A, n, "A");
    print_mat(info->B, n, "B");
    f(info);
    print_mat(info->C, n, "C");
  
}
   
int main(int argc, char* argv[]){
    dgemm_info info;
    int n, bs;

    if(argc != 3){
        printf("Usage: ./a.out [n] [block size]\n");
        exit(1);
    }else{
        n = atoi(argv[1]);
        bs = atoi(argv[2]);
        info.n = n;
        info.bs = n;
        omp_set_num_threads(4);
    }

    if( n % bs != 0 ){
        printf("n must be multiple of block size\n");
        exit(1);
    }

    create_col_mat(&info);
    //WARNING
    //Don't forget that dgemm_naive uses the block-size to know how far to 
    //travel, so if blocksize isn't n when dgemm_naive is called then you
    //will get an incorrect result
    //info.bs = bs;
    //
    //test_dgemm(&dgemm_omp, &info);

    run_timings(&info, bs);

    free_mat(&info);
}

