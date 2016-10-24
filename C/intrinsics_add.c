#include <stdio.h>
#include <immintrin.h>

/* 
 * This must be compiled with the flags
 * -march=native -std=c99
 *  Otherwise the compiler won't detect AVX and will yell
 *  about declaring i in a loop.
 */

int main(){

    double a[] = {4,5,6,7};
    double b[] = {8,9,10,11};
    double c[4];

    __m256d ap, bp, cp;

    ap = _mm256_loadu_pd(a);
    bp = _mm256_loadu_pd(b);

    cp = _mm256_add_pd(ap, bp);
    _mm256_storeu_pd(c, cp);

    for(int i=0; i<4; i++){
        printf("%d: %g\n", i, c[i]);
    }


    printf("Hello, world!\n");

}
