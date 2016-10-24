import lombok.Data;

@Data
public class DenseVector {

   private final int size;
   private final double[] values;

   public double getValue(int i){
      return values[i];
   }
}
