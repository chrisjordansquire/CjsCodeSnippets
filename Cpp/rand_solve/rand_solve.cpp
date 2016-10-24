#include <iostream>
#include <Eigen/Dense>
#include <ctime>
#include <cstdio>

// Testing out Eigen
// Pretty neat library

#define START start = clock();
#define END printTime(clock()-start);

using namespace Eigen;
using namespace std;


void printTime(clock_t diff){
	int msec = diff*1000 / CLOCKS_PER_SEC;
	printf("Time taken: %d milliseconds\n ", msec);
}

void printResidual(VectorXf real_x, VectorXf solved_x){
	double residual = (real_x-solved_x).norm();
	printf("The residual is %g\n", residual);

}

//I thought I could use this to eliminate the ugly macro's
//But I couldn't figure out how to time the factorization, since I
//was passing that in as well
template <typename T>
void timedResidualTest(MatrixXf A, T factorizedA, VectorXf real_x, VectorXf b, string msg){
    clock_t start = clock();
    cout << "------------------------"<<endl;
    cout << msg << endl;
    VectorXf solved_x = factorizedA.solve(b);
    cout<<"x: ";
    printResidual(real_x, solved_x);
    cout<<"b: ";
    printResidual(b, A*solved_x);
    printTime(clock() - start);
}

int main(int argc, char* argv[]){

    if(argc<2){
        std::cout << "Usage: ./a.out size-of-matrix" << std::endl;
        exit(1);
    }

  	int const N = atoi(argv[1]);

	MatrixXf A = 10*MatrixXf::Random(N, N);
	VectorXf real_x = 10*VectorXf::Random(N);

	VectorXf b = A * real_x;
/*
	cout << real_x << endl;
	cout << "------------------" << endl;
	cout << A << endl;
	cout << "------------------" << endl;
	cout << b << endl;
*/
	cout << "||x||=" << real_x.norm() << endl;
	cout << "||A||=" << A.norm() << endl;
	cout << "||b||=" << b.norm() << endl;

	clock_t start;

	START
	cout << "-----------------------"<<endl;
  	cout << "partial pivot lu" << endl;
	VectorXf pplu_x = A.partialPivLu().solve(b);
	printResidual(real_x, pplu_x);
	printResidual(A*pplu_x, b);
    END

	START
	cout << "-----------------------"<<endl;
	cout << "full pivot lu" << endl;
	VectorXf fplu_x = A.fullPivLu().solve(b);
	printResidual(real_x, fplu_x);
	printResidual(A*fplu_x, b);
	END

	START
	cout << "-----------------------"<<endl;
	cout << "householder reflection qr" << endl;
	VectorXf hhqr_x = A.householderQr().solve(b);
	printResidual(real_x, hhqr_x);
	printResidual(A*hhqr_x, b);
	END

	START
	cout << "-----------------------"<<endl;
	cout << "column pivot householder qr" << endl;
	VectorXf cphhqr_x = A.colPivHouseholderQr().solve(b);
	printResidual(real_x, cphhqr_x);
	printResidual(A*cphhqr_x, b);
	END

	START
	cout << "-----------------------"<<endl;
	cout << "full pivot householder qr" << endl;
	VectorXf fphhqr_x = A.fullPivHouseholderQr().solve(b);
	printResidual(real_x, fphhqr_x);
	printResidual(A*fphhqr_x, b);
	END

}


