; The comands to build, compile/link, and run are
; nasm -fmacho64 add_integers.s
; gcc add_integers.o
; ./a.out 4 10 3


global _main
extern _atoi
extern _printf


section .text

_main:
    push rbx ; done for stack alighment so we can call stuff
    
    dec rdi
    mov r12, 0 ; r12 is safe to use as accumulator since it's
               ; preserved across calls
    jz nothingToSum

accumulate:
    push rdi
    push rsi
    mov rdi, [rsi + rdi*8]
    call _atoi
    pop rsi
    pop rdi
    add r12, rax
    dec rdi
    jnz accumulate

print:
    lea rdi, [format]
    mov rsi, r12
    mov rax, 0 ; for varargs functions, says nothign is in the floating
               ; point (aka 'vector') registers
    call _printf
    jmp done

nothingToSum:
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
; 10 is ASCII for 'line feed', i.e. new line.
; And 0 is the null-termination of the format string.
format: db "%d", 10, 0 
error: db "There are no commnand line arguments to sum.", 10, 0




