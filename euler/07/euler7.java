import java.lang.*;
import java.util.*;

public class euler7{

    public static long[] primesUpToNth(long N){
        assert N>2;

        long [] primes = new long[(int )N];
    
        primes[0] = 2;
        int nthPrime=1;
        int i=3;


        while(nthPrime != N){
            int j=0;
            boolean isPrime=true;

            while(Math.sqrt(primes[j])+1 < i && j < nthPrime){
                if( i % primes[j] == 0 ){
                    isPrime=false;
                    break;
                }
                j++;
            }

            if( isPrime ){
                primes[nthPrime] = i;
                nthPrime++;
            }else{
                i++;
            }
        }

        return primes;

    }

    public static void main(String[] args){

        int N;

        if(args.length > 0){
            N = Integer.parseInt(args[0]);
        }else{
            N = 10001;
        }
        System.out.println("N is " + N);

        System.out.println("The Nth prime is "+euler7.primesUpToNth(N)[N-1]);
    }
}

