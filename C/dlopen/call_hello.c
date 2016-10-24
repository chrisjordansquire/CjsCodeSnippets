#include <dlfcn.h>
#include <stdlib.h>
#include <stdio.h>

// A simple example to show myself how dynamic linking works.
// Pretty cool.
// (Famous last words before hitting dll hell)

typedef int (*pf)(char*);

int main(){
    void* lib;
    pf greet;
    char name[] = "Christopher";

    lib = dlopen("hello.so", RTLD_NOW);
    
    greet = (pf) dlsym(lib, "hello");

    greet(name);

    greet = (pf) dlsym(lib, "hello2");
    if( greet == NULL ){
        printf("There was a linking error\n");
        char* errstr;
        errstr = dlerror();
        printf("Error: %s\n", errstr);
    }
    
    dlclose(lib);

    return 0;
}
