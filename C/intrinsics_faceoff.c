#include <xmmintrin.h>
#include <pmmintrin.h>
#include <string.h>
#include <time.h>
#include <stdio.h>

// Riffing on example code from this slide deck:
// https://www.inf.ethz.ch/personal/markusp/teaching/263-2300-ETH-spring12/slides/class15.pdf

typedef void (*vec_func)(float*, float*, int);

void time_vec_func(float *x, float* y, int n, vec_func f){
    clock_t start = clock();
    for(int i=0; i<100; i++){
        f(x, y, n);
    }
    int msec = (clock()-start) * 1000 / CLOCKS_PER_SEC;
    printf("Time taken: %d milliseconds\n", msec);
}

void lp_vec(float *x, float *y, int n){
    __m128 half, v1, v2, avg;

    half = _mm_set1_ps(0.5);
    for(int i=0; i< n/8; i++){
        v1 = _mm_load_ps(x+i*8);
        v2 = _mm_load_ps(x+4+i*8);
        avg = _mm_hadd_ps(v1, v2);
        avg = _mm_mul_ps(avg, half);
        _mm_store_ps(y+i*4, avg);
    }
}

void lp(float *x, float *y, int n){
    for(int i=0; i<n/2; i++){
        y[i] = (x[2*i]+x[2*i+1])/2;
    }
}

int main(){

    const int N = 1048576;

    float x[N], y[N/2];
    time_t start, end;

    for(int i=0; i<N; i++){
        x[i] = i;
    }
    
    memset(y, 0, sizeof(float)*N/2);

    time_vec_func(x, y, N, &lp);

    time_vec_func(x, y, N, &lp_vec);
}

