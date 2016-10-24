#include <cstdlib>
#include <cstdio>

int palindrome(int x){
	int y=0;
	while(x != 0){
		y = y*10 + x%10;
		x = (x - x%10)/10;
	}
	return y;
}

bool isPalindrome(int x){
	return x == palindrome(x);
}

int main(){
	const int upper = 1000;
	int largest = 0;


	for(int i=0; i<upper; i++){
		for(int j=0; j<=i; j++){
			if(isPalindrome(i*j) && i*j>largest){
				largest = i*j;
			}
		}
	}
	printf("The largest palindrome is %d\n",largest);
}
