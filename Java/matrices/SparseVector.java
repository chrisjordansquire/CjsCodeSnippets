package com.chrisjs.matrices;

import lombok.Data;

@Data
public class SparseVector {

    private final int size;
    private final int[] indices;
    private final double[] values;

    public DenseVector toDenseVector(){

        double[] denseValues = new double[size];
        for(int i=0; i<indices.length; i++){
            denseValues[indices[i]] = values[i];
        }

        return new DenseVector(size, denseValues);
    }

}
