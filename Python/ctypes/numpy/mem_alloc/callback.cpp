#include <stdio.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef void*(*allocator_t)(int, int*);

void foo(allocator_t allocator) {
   int dim = 2;
   int shape[] = {2, 3};
   float* data = NULL;
   int i, j;
   printf("foo calling allocator\n");
   data = (float*) allocator(dim, shape);
   printf("allocator returned in foo\n");
   printf("data = 0x%p\n", data);
   for (i = 0; i < shape[0]; i++) {
      for (j = 0; j < shape[1]; j++) {
         *data++ = (i + 1) * (j + 1);
      }
   }
}

#ifdef __cplusplus
}
#endif
