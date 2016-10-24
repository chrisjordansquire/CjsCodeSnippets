import java.lang.*;
import java.util.*;
import java.io.*;

public class euler1{

	public static void main(String[] args){
	
		final int upper = 1000;
		int sum=0;
		for(int i=0; i<upper; i++){
			if(i%3==0 || i%5==0){
				sum += i;
			}
		}

		System.out.println("The sum is "+ sum);
	}
}
