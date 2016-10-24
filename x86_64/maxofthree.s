; Comes from http://cs.lmu.edu/~ray/notes/nasmtutorial/
; This is meant to be used with callmaxofthree.c
; The C code calls this assembly code.
; The commands to build, compiled/link, and run are
;
; ~/bin/nasm-2.10.09/nasm -fmacho64 maxofthree.s 
; gcc callmaxofthree.c maxofthree.o
; ./a.out
;
; NOTE: The underscore in the exported name is necessary to match the
; name the linker will look for. Without it the linking fails with
; the error that the function _maxofthree being used in _main 
; (i.e., in the C file) can't be found.


global _maxofthree
default rel

section .text

_maxofthree:
    mov rax, rdi
    cmp rax, rsi
    cmovl rax, rsi
    cmp rax, rdx
    cmovl rax, rdx
    ret
