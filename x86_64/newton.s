; This does a single iteration of Newton's method for square roots 
; The comands to build, compile/link, and run are
; nasm -fmacho64 newton.s
; gcc add_integers.o
; ./a.out 4 10 3


global _main
extern _atof
extern _printf


section .text

_main:
    ; When _main is hit, the input arguments are 
    ; argc in rdi and argv in rsi
    push rbx ; done for stack alighment so we can call stuff
    
    ; Usage is ./a.out root initial
    dec rdi
    cmp rdi, 2
    jne tooFewArguments

readArguments:
    ; rdi and rsi need pushed before calling atof because those registers
    ; are caller saved, and they're being used.
    push rdi
    push rsi
    mov rdi, [rsi + rdi*8]
    call _atof
    ; processing arguments backwards
    ; xmm2 is the initial guess
    movsd xmm2, xmm0
    
    pop rsi
    pop rdi

    dec rdi
    mov rdi, [rsi + rdi*8]

    push rsi
    push rdi

    call _atof
    ; xmm1 will be the number to take the sqrt of
    movsd xmm1, xmm0

    pop rsi
    pop rdi

newton:
    
    movsd xmm3, [half]
    mulsd xmm1, xmm3
    divsd xmm1, xmm2
    mulsd xmm2, xmm3
    addsd xmm1, xmm2

print:
    movsd xmm0, xmm1
    lea rdi, [format]
    mov rsi, r12
    mov rax, 1 ; for varargs functions, says nothign is in the floating
               ; point (aka 'vector') registers
    call _printf
    jmp done

tooFewArguments:
    lea rdi, [error]
    xor rax, rax
    call _printf

done:
    pop rbx
    ret

; The default rel directive is apparently only meant to be applied
; to the data section.
; (This might not be obvious in many examples online, since generally
; people put the data section before the text section.) 
default rel
section .data

; This defines a series of bytes. 
; (I belive "define bytes" is what db stands for.)
; 10 is ASCII for 'line feed', i.e. new line.
; And 0 is the null-termination of the format string.
format: db "%g", 10, 0 
error: db "Wrong number of arguments.", 10, 0
half: dq 0.5
