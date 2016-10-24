; Compile and run with
; nasm -fmacho64 1.s && gcc 1.o && ./a.out
; (don't use the stock version of nasm on OSX, though)
global _main
default rel
extern _printf

section .text

_main:
    mov r12, 1
    mov r13, 0
    sub rsp, 8
    
loop:
   
test:
    mov rax, r12
    xor rdx, rdx
    mov r9, 3
    div r9
    cmp rdx, 0
    je accumulate
    
    mov rax, r12
    xor rdx, rdx
    mov r9, 5
    div r9
    cmp rdx, 0
    je accumulate

    jmp end_test

accumulate:
    add r13, r12
 
end_test:
    inc r12
    cmp r12, 1000
    jl loop

end:
    lea rdi, [format]
    mov rsi, r13
    call _printf

    add rsp, 8
    ret

section .data
    format: db "The sum is %u",10,0
