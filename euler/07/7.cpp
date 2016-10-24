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

	for(int i=0; i<10000; i++){
		gen.nextPrime();
	}
	printf("The 10001st prime number is %d\n", gen.nextPrime());
}









