import lombok.Data;

@Data
public class DenseMatrix {

    private final int rows;
    private final int columns;
    private final double[] values;

    public double getValue(int row, int column){
        return values[row*columns + column];
    }

    public DenseVector lowerTriangularSolve(DenseVector b){
        // Solve assuming matrix is lower triangular.
        assert(b.getSize() == rows);
        assert(rows == columns);

        double[] xValues = new double[b.getSize()];
        System.arraycopy(b.getValues(), 0, xValues, 0, b.getSize());
        for(int i=0; i<b.getSize(); i++){
            xValues[i] = xValues[i] / this.getValue(i, i);
            for(int j=i+1; j<b.getSize(); j++){
                xValues[j] -= xValues[i] * this.getValue(j, i);
            }
        }

        return new DenseVector(b.getSize(), xValues);
    }

    public DenseMatrix choleskyFactorization(){
        //TODO
        return null;
    }
}
