#include <cmath>
#include <iostream>

int main(){

	long long num = 600851475143;

	printf("The number is %lld\n", num);
	
	const long long upper = sqrt(num);
	long max = 0;

	for(long i=2; i<upper; i++){
		if(num % i==0){
			max = i;
			while(num % i ==0){
				num /= i;
			}
		}
	}
	
	printf("The largest prime divisor of %lld is %ld\n",num,max); 

}
