#ifdef __cplusplus
extern "C"{
#endif

#include<math.h>

typedef double realfunction(double x);

int npow;

// Simple esimation of integral of F between x1 and x2 using N points

double rectquad (realfunction F, double x1, double x2, int N){
    double dA;
    double result = 0.0;
    double dx = (x2-x1)/N;
    double x = x1;
    int i;

    for(i=0; i<N; i++){
        dA = F(x+dx/2)*dx;
        result += dA;
        x += dx;
    }
    return result;
}

double samplefun1(double x){
    return x+2*x*x;
}

double samplefun2(double x){
    return x+npow*pow(x,npow);
}

#ifdef __cplusplus
}
#endif
