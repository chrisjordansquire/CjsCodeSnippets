import java.util.Random;
import java.lang.System;

public class PrimDoubleArr{
    // Checking how fast matrix multiplication w/ primitive double arrays is
    // Spoiler: It's a lot faster.

    static Random generator = new Random();

    public static double nextDouble(){
        return PrimDoubleArr.generator.nextDouble();
    }

    public static void fill(double[][] arr){
        int N = arr.length;
        
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                arr[i][j] = PrimDoubleArr.nextDouble();
            }
        }

    }
   
    public static void mult(double [][] arr1, double [][] arr2, 
            double [][] out){

        int N = arr1.length;

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                for(int k=0; k<N; k++){
                    out[i][j] += arr1[i][k] * arr2[k][j];
                }
            }
        }
    }

    public static void main(String []args){

        final int N = Integer.parseInt(args[0]);

        long start = System.nanoTime();

        double [][] arr1 = new double[N][N];
        double [][] arr2 = new double[N][N];

        long end = System.nanoTime();
        System.out.println("Initialize: " + 1e-9 * (end - start)/2);

        start = System.nanoTime();

        PrimDoubleArr.fill(arr1);
        PrimDoubleArr.fill(arr2);
        end = System.nanoTime();
        System.out.println("Fill:       " + 1e-9*(end-start)/2);

        double [][] out = new double[N][N];
        start = System.nanoTime();
        
        PrimDoubleArr.mult(arr1, arr2, out);

        end = System.nanoTime();
        System.out.println("Multiply:   " + 1e-9 * (end-start));
    }
}

