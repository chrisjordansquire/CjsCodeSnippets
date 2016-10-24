#include <stdio.h>

#ifdef __cplusplus
extern "C" {
#endif

int bar(double* data, int len) {
   int i;
   printf("data = %p\n", (void*) data);
   for (i = 0; i < len; i++) {
      printf("data[%d] = %f\n", i, data[i]);
   }
   printf("len = %d\n", len);
   return len + 1;
}

#ifdef __cplusplus
}
#endif
