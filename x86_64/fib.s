;Comes from the nasm tutorial http://cs.lmu.edu/~ray/notes/nasmtutorial/
;This can be assembled, linked, and run with this command
;nasm -fmacho64 fib.s && gcc fib.o && ./a.out

global _main
extern _printf
default rel

section .text

_main:
    
    push rbx

    mov ecx, 90
    xor rax,rax
    xor rbx,rbx
    inc rbx

print:
    
    push rax
    push rcx

    lea rdi, [format]
    mov rsi, rax
    xor rax, rax

    call _printf

    pop rcx
    pop rax

loop:
    mov rdx, rax
    mov rax, rbx
    add rbx, rdx
    dec ecx
    jnz print

    pop rbx
    ret

section .data
    ;Note use of l ("ell") in the format string
    ;this ensures the value is printed as a long
    ;rather than as a 32-bit interer. Without
    ;this the fibonnaci numbers will overflow a
    ;bit before the 50th one. 
    format: db "%20lu",10,0
