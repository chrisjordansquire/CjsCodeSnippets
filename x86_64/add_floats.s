; The comands to build, compile/link, and run are
; nasm -fmacho64 add_integers.s
; gcc add_integers.o
; ./a.out 4 10 3


global _main
extern _atof
extern _printf


section .text

_main:
    ; When _main is hit, the input arguments are 
    ; argc in rdi and argv in rsi
    ; So rdi is decremented as arguments are processed,
    ; while rsi is used when determining where the pointer
    ; is that should be passed into atof
    push rbx ; done for stack alighment so we can call stuff
    
    dec rdi
    ; initialize xmm0 with double precision
    ; movsd -> "move scalar double"
    ; The precision must be doulbe since printf can only 
    ; print doubles. 
    ; This is actually a language-level restiction: all arguments
    ; to varargs functions are promoted to double.
    movsd xmm1, [initial_zero]
    jz nothingToSum

accumulate:
    ; rdi and rsi need pushed before calling atof because those registers
    ; are caller saved, and they're being used.
    push rdi
    push rsi
    mov rdi, [rsi + rdi*8]
    call _atof
    addsd xmm1, xmm0
    ; NOTE: This loop coudl also have been implemented using
    ; movsd xmm1, [sum]
    ; addsd xmm1, xmm0
    ; movsd [sum], xmm1
    ; where sum was initialized data to 0.
    ; The advantage of that implementation is it would be guaranteed
    ; to work even if the function being called used the xmm1
    ; register. In the System V ABI, none of the floating point
    ; registers are guaranteed to be untouched across calls. 
    ; (Also, oddly, push and pop only seem to work for the non-floating
    ; point registers. But that's ok since using mov works fine, too,
    ; at least if you have a place to put the data. In fact, it's not
    ; clear at all that mov is slower/less desirable than push/pop in
    ; these situations.)
    pop rsi
    pop rdi
    dec rdi
    jnz accumulate

print:
    movsd xmm0, xmm1
    lea rdi, [format]
    mov rax, 1 ; for varargs functions, says nothign is in the floating
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
; (I belive "define bytes" is what db stands for.)
; 10 is ASCII for 'line feed', i.e. new line.
; And 0 is the null-termination of the format string.
format: db "%g", 10, 0 
error: db "There are no commnand line arguments to sum.", 10, 0
; Apparently the dx directives are used to 'declare initialized data'
; So, explicitly for the .data section, I think.
; There are other directives , redx, "re" for reserve, that declare
; unitialized data, for the .bss section.
; Note that the period when defining floating point constant is mandatory,
; as othrewise nasm will think it is a higher precision integer constant.
initial_zero: dq 0.0

