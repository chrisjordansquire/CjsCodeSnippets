import java.lang.*;
import java.util.*;
import java.io.*;
import java.math.*;

public class euler3{

	public static void main(String[] args){

		BigInteger num = new BigInteger("600851475143");

		long max=0;
		int i=1;

		while(!num.equals(BigInteger.valueOf(1))){
			i++;
			//System.out.println(i + " " + num);
			if(num.mod(BigInteger.valueOf(i)).equals(BigInteger.valueOf(0))){
				//System.out.println(i+" is a factor");
				max = i;
				while(num.mod(BigInteger.valueOf(i)).equals(BigInteger.valueOf(0))){
					//System.out.println(i+" is still a factor");
					num=num.divide(BigInteger.valueOf(i));
				}
			}
		}

		System.out.println("The max is " + max);
	}
}
