; from http://cs.lmu.edu/~ray/notes/nasmtutorial/
global _add_four_floats
default rel

section .text

_add_four_floats:
    movdqa xmm0, [rdi]
    movdqa xmm1, [rsi]
    addps xmm0, xmm1
    movdqa [rdi], xmm0
    ret
