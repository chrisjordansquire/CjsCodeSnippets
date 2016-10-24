import std.stdio;

uint palindrome(uint x){
	int y=0;
	while(x != 0){
		y = y*10 + x%10;
		x = (x - x%10)/10;
	}
	return y;
}

bool isPalindrome(uint x){
	return x == palindrome(x);
}

void main(){
	const int upper = 1000;
	int largest = 0;


	for(int i=0; i<upper; i++){
		for(int j=0; j<=i; j++){
			if(isPalindrome(i*j) && i*j>largest){
				largest = i*j;
			}
		}
	}
	writefln("The largest palindrome is %d",largest);
}
