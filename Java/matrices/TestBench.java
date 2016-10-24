import com.chrisjs.matrices.DenseMatrix;
import com.chrisjs.matrices.DenseVector;
import com.chrisjs.matrices.SparseMatrix;
import com.chrisjs.matrices.SparseVector;

public class TestBench {

    public static void main(String[] args){

        DenseVector b = new DenseVector(2, new double[]{2.0, 3.0});
        DenseMatrix A = new DenseMatrix(2, 2, new double[]{3.0, 1.0, 1.0, 2.0});

        System.out.println(b.toString());
        System.out.println(A.toString());
        System.out.println(A.lowerTriangularSolve(b));


        SparseVector bSparse = new SparseVector(8, new int[]{1, 3, 7}, new double[]{3.0, 4.0, 5.0});
        SparseMatrix ASparse = new SparseMatrix(8, 8,
                new int[]{0,    2,    4, 5, 6,    8,    10, 11, 12},
                new int[]{0, 4, 1, 5, 2, 3, 4, 7, 5, 6, 6, 7},
                new double[]{1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0});
        System.out.println(bSparse);
        System.out.println(ASparse);
        System.out.println(ASparse.reach(bSparse));

        DenseVector bDense = new DenseVector(8, new double[]{0, 1, 2, 3, 4, 5, 6, 7});
        System.out.println(ASparse.lowerTriangularSolve(bDense));
    }
}
