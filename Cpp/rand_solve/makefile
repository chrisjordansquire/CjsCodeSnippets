
EIGEN=$(HOME)/devel/packages/eigen

intel-opt: CFLAGS=-O2 -DNDEBUG  
intel-opt: intel

intel-opt3: CFLAGS=-O3 -DNDEBUG -xHOST
intel-opt3: intel

intel: CC=icpc
intel: W=-w
intel: program

#Looks like adding -msse2 or -msse4 doesn't matter
gnu-ultra: CFLAGS=-DNDEBUG -m64 -O3 -Ofast -flto -march=native -funroll-loops

gnu-ultra: gnu

gnu-opt3: CFLAGS=-O3 -DNDEBUG -march=native
gnu-opt3: gnu

gnu-opt: CFLAGS=-O2 -DNDEBUG 
gnu-opt: gnu

gnu: CC=g++
gnu: program

ngnu-ultra: CFLAGS=-DNDEBUG -m64 -O3 -Ofast -flto -march=native -funroll-loops
ngnu-ultra: ngnu
ngnu: CC=ng++
ngnu: program

program:
	$(CC) $(CFLAGS) $(W) -I$(EIGEN) rand_solve.cpp -o a.out 

