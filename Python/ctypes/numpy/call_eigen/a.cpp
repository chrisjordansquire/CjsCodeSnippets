extern "C" 
{
	float sum_float_numpy_array(float* a, int n);
    void sum_double_numpy_array(double* a, double* b, double* out, int n);
}


#include <Eigen/Core>
using namespace Eigen;


float sum_float_numpy_array(float* a, int n)
{
	Map<VectorXf> bubi(a, n);
	return bubi.sum();
}

void sum_double_numpy_array(double* a, double* b, double *out, int n){
    Map<VectorXd> A(a, n);
    Map<VectorXd> B(b, n);
    Map<VectorXd> Out(out, n);

    Out = A + B;
}
