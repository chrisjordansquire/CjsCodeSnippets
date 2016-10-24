import std.stdio;
import std.conv;
import std.math;

class primeGen{

    private:
        int[] primes = [2];
        bool testPrime(int n){
            foreach( int p ; primes ){
                if( n%p == 0 ) return false;
                if( p > sqrt(to!float(n)) ) break; 
            }
            return true;
        }

    public:
        int nextPrime(){
            int i = primes[$-1];
            bool isPrime = false;

            while(!isPrime){
                i++;
                isPrime = testPrime(i);
            }

            primes ~= i;
            return i;
        }
}

void main(string args[]){
    
    auto gen = new primeGen;
    int n; 

    if(args.length > 1){
        n = to!int(args[1]);
    }else{
        n=9999; //Array starts w/ first prime: 2
    }
    foreach(i ; 0..n){
        gen.nextPrime();
    }
    writeln("The 10001st prime number is ", gen.nextPrime());

}
