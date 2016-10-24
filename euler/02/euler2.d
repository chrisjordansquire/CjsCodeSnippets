import std.stdio;
import std.math;

void main(){

	const int upper = 4*pow(10,6);

	int sum=0, f1=1, f2=2;

	while(f2<upper){
		if(f2 % 2 == 0){
			sum += f2;
		}
		f2 = f1 + f2;
		f1 = f2 - f1;
	}
	writefln("The sum is %d", sum);

}
