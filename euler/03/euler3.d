import std.math;
import std.stdio;

void main(){

	ulong num = 600851475143;

	writefln("The number is %d\n", num);
	
	immutable ulong upper = (cast(ulong) sqrt(cast(real)num)) + 1;
	ulong max = 0;

    ulong factor = num;

	for(ulong i=2; i<upper; i++){
		if(factor % i==0){
			max = i;
			while(factor % i ==0){
				factor /= i;
			}
		}
	}
	
	writefln("The largest prime divisor of %d is %d\n",num,max); 

}
