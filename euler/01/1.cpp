#include <cstdio>
#include <cstdlib>

int main(int argc, char* argv[]){
	
	int upper;

	if(argc < 2){
		upper = 1000;
	}else{
		upper = atoi(argv[1]);
	}
	int sum = 0;

	int i=1;
	while(3*i < upper){
		sum += 3*i;
		++i;
	}
	
	i=1;
	while(5*(i+1)<upper){
		sum+= 5*(2*i+1);
		i+=3;
	}

	if(5*i<upper){
		sum += 5*i;
	}

	printf("The sum is %d\n", sum);
}
		


