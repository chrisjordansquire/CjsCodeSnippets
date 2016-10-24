import lombok.Data;

import java.util.*;

@Data
public class SparseMatrix {

    private final int rows;
    private final int columns;
    private final int[] columnStartIndices;
    private final int[] rowIndices;
    private final double[] values;


    public DenseVector upperTriangularSolve(DenseVector b){
        //TODO
        return null;
    }

    public DenseVector lowerTriangularSolve(DenseVector b){
        assert(b.getSize() == rows);
        assert(rows == columns);

        double[] xValues = new double[b.getSize()];
        System.arraycopy(b.getValues(), 0, xValues, 0, b.getSize());
        for(int i=0; i<b.getSize(); i++){
            //This uses that the first entry in any column will be the diagonal
            xValues[i] = xValues[i] / this.values[columnStartIndices[i]];
            System.out.println("foo: " + this.values[columnStartIndices[i]]);
            for(int j=columnStartIndices[i]+1;
                    j<columnStartIndices[i+1];
                    j++){
                xValues[this.rowIndices[j]] -= xValues[i] * this.values[j];
                System.out.println(Arrays.toString(xValues));
            }
        }

        return new DenseVector(b.getSize(), xValues);
    }

    public SparseVector lowerTriangularSolve(SparseVector b){
        //TODO
        return null;
    }

    public SparseMatrix choleskyFactorization(){
        //TODO
        return null;
    }

    public int[] reach(SparseVector b){
        Set<Integer> solutionIndices = new HashSet<>();
        Set<Integer> visitedIndices = new HashSet<>();
        int[] rhsIndices = b.getIndices();
        Stack<Integer> reachStack = new Stack<>();
        for(int i=rhsIndices.length-1; i>=0; i--){
            reachStack.push(rhsIndices[i]);
            solutionIndices.add(rhsIndices[i]);
            visitedIndices.add(rhsIndices[i]);
        }

        while(!reachStack.empty()){
            int columnIndex = reachStack.pop();
            for(int rowIndexIndex=columnStartIndices[columnIndex];
                    rowIndexIndex<columnStartIndices[columnIndex+1];
                    rowIndexIndex++){
                int rowIndex = rowIndices[rowIndexIndex];

                if(!solutionIndices.contains(rowIndex)){
                    solutionIndices.add(rowIndex);
                    if(!visitedIndices.contains(rowIndex)){
                        visitedIndices.add(rowIndex);
                        reachStack.push(rowIndex);
                    }
                }
            }
        }

        System.out.println("ra: " + solutionIndices);

        //http://stackoverflow.com/a/23945015
        return solutionIndices.stream().mapToInt(i->i).toArray();
    }
}
