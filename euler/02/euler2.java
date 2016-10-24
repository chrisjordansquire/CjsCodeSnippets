import java.lang.*;
import java.util.*;
import java.io.*;
//import java.math;

public class euler2{

	public static void main(String[] args){
		final int upper = 4 * (int) Math.pow(10,6);

		int sum=0, f1=1, f2=2;
		while(f2 < upper){
			if( f2 % 2==0){
				sum+=f2;
			}
			f2 = f1+f2;
			f1 = f2-f1;
		}
		System.out.println("The sum is "+sum);

	}
}
