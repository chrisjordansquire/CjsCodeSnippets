import java.lang.*;
import java.util.*;

public class euler4{

	public static int palindrome(int x){
		int y=0;
		while(x != 0){
			y = y*10 + x%10;
			x = (x - x%10)/10;
		}
		return y;
	}

	public static boolean isPalindrome(int x){
		return x == euler4.palindrome(x);
	}

	public static void main(String [] args){
		final int upper = 1000;
		int largest = 0;


		for(int i=0; i<upper; i++){
			for(int j=0; j<=i; j++){
				if(euler4.isPalindrome(i*j) && i*j>largest){
					largest = i*j;
				}
			}
		}
		System.out.println("The largest palindrome is "+largest);
	}

}
