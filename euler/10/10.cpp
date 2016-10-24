#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <cmath>

class primeGen{
	private:
		std::vector<int> primes;
		bool testPrime(int n);
	public:
		int nextPrime();

};

bool primeGen::testPrime(int n){ 
	std::vector<int>::iterator iter;
	
	for(iter = primes.begin(); iter != primes.end(); iter++){
		if( n%(*iter)==0) return false;
		if( *iter > sqrt(n) ) break;
	}
	
	return true;
};

int primeGen::nextPrime(){
	if(primes.size()==0){
		primes.push_back(2);
		return 2;
	}else{
		int i = primes.back();
		bool isPrime=false;

		while(!isPrime){
			i++;
			isPrime = testPrime(i);
		}

		primes.push_back(i);
		return i;
	}
}

int main(){

	primeGen gen;
	long sum=0;
	int tmp=gen.nextPrime();
	const int upper = 2*pow(10,6);

	while(tmp<upper){
		sum += tmp;
		tmp = gen.nextPrime();
	}
	printf("The sum is %ld\n", sum);
}









