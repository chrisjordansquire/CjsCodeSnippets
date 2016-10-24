import java.lang.Double;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.lang.System;

public class DoubleArr{
    // Checking how fast matrix multiplcation with Java object doubles is

    static Random generator = new Random();

    public static double nextDouble(){
        return DoubleArr.generator.nextDouble();
    }

    public static void fill(List<List<Double>> arr){
        int N = arr.size();
        
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                arr.get(i).add( DoubleArr.nextDouble());
            }
        }

    }
   
    public static void mult(List<List<Double>> arr1, List<List<Double>> arr2, 
            List<List<Double>> out){

        int N = arr1.size();

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                for(int k=0; k<N; k++){
                    out.get(i).set(j,
                            arr1.get(i).get(k) + arr2.get(k).get(j));
                }
            }
        }
    }

    public static void main(String []args){

        final int N = Integer.parseInt(args[0]);

        long start = System.nanoTime();

        List<List<Double>> arr1 = new ArrayList<List<Double>>();
        List<List<Double>> arr2 = new ArrayList<List<Double>>();

        for(int i=0; i<N; i++){
            arr1.add(new ArrayList<Double>());
            arr2.add(new ArrayList<Double>());
        }

        long end = System.nanoTime();
        System.out.println("Initialize: " + 1e-9 * (end - start)/2);

        start = System.nanoTime();

        DoubleArr.fill(arr1);
        DoubleArr.fill(arr2);
        end = System.nanoTime();
        System.out.println("Fill:       " + 1e-9*(end-start)/2);

        List<List<Double>> out = new ArrayList<List<Double>>();
        for(int i=0; i<N; i++){
            out.add(new ArrayList<Double>());
        }
        DoubleArr.fill(out);

        start = System.nanoTime();
        
        DoubleArr.mult(arr1, arr2, out);

        end = System.nanoTime();
        System.out.println("Multiply:   " + 1e-9 * (end-start));
    }
}

