; A port of code in the nasm tutorial for linux (http://cs.lmu.edu/~ray/notes/nasmtutorial/)
; to work on mac
; Note that this is meant to be linked using gcc rather than ld, just because
; figuring out the exact linker options to link in the c standard library
; is rather annoying. (Though I believe it can be done using the -v option
; in gcc.)

; This can be compiled via
; nasm -fmacho64 call_puts.s
; gcc call_puts.o

; NOTE: I'm using _main as the starting point here since gcc is doing the
; linking, and gcc expects that to be the starting point of the file
; when invoked.

global _main
extern _puts
default rel

section .text

_main: 

    push rbx ;done for stack alignment
    lea rdi, [message] ;according to x64 calling conventions on SysV systems, 
                       ;rdi is the location of the first argument.
                       ;NOTE: Apparently we can't load message as below
                       ;mov rdi, message 
                       ;if message isn't declared as data. Also, doing the
                       ;mov instruction instead of lea leads to a warning about
                       ;PIE disabled. AFAIU, this somehow relates to mac not
                       ;supporting absolute addressing.
    call _puts

done:
    pop rbx
    ret

section .data
    message: db "Hola, mundo", 0
