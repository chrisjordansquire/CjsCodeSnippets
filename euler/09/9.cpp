#include<stdio.h>
#include <algorithm>

int main(){
    int required_pythagorean_triplet_sum = 1000;
    int a, b, c;

    for(int i=0; i < required_pythagorean_triplet_sum; i++){
        int j_max = std::min(i, required_pythagorean_triplet_sum - i);
        for(int j=0; j < j_max; j++){
            int third_side = required_pythagorean_triplet_sum - i - j; 
            if(i * i + j * j == third_side * third_side){
                a = i;
                b = j;
                c = third_side;
                goto exit_loop;
            }
        }
    }

exit_loop:
    printf("The tuple is (%d, %d, %d)\n", a, b, c);
    printf("The product is %d\n", a * b * c);

}
