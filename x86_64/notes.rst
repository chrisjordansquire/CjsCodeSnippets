x86-64 Notes
============

Finding x86-64 information, especially for mac's, has proven to be surprisingly
difficult. So I'm compiling information, including links, here for future
reference. 

Examples
--------
Finding relevant examples online can be really difficult, but you can always
generate your own by having the compiler dump the assembly of a C file. This
can even be done in nasm/intel syntax instead of gcc/AT&T syntax.

http://stackoverflow.com/questions/10990018/how-to-generate-assembly-code-with-clang-in-intel-syntax

Floating Point registers
------------------------
Floating point operations have their own registers. Surprisingly, there are 3-ish
separate implementations of floating point operations on x86 processors. The first
is, more-or-less, legacy and rarely used. This is the x87 floating point
coprocessor instructions. These operate on registers

The SSE/SSE2 instructions were a complete reworking, and they came


References:
Discusses evolution of floating point on x86 processors.
https://www.cs.uaf.edu/2012/fall/cs301/lecture/11_02_other_float.html

Stack
-----
The program stack is an area of memory* pointed to by the stack pointer. It's
where data can be shoved temporarily before being reclaimed. (This is useful
when calling functions, for example.) Push pushes the contents of a register
to the stack, and pop pops the top of the stack to a register. Note that push
and pop are completely equivalent to copying the top to/from the stack and moving
the stack pointer.

* This literally means main memory. It typically won't go all the way to main
  memory because of the cache hierarchy, though.

References:
Wikipedia's article on stacks includes a section on hardware stacks.
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)#Hardware_stacks
This also has a great explanation
https://en.wikibooks.org/wiki/X86_Disassembly/The_Stack

Calling Convention
------------------
Calling conventions state where arguments to C functions go when making
a call. 64-bit Mac OSX and Linux use System V ABI calling conventions.

http://stackoverflow.com/questions/2535989/what-are-the-calling-conventions-for-unix-linux-system-calls-on-x86-64
http://wiki.osdev.org/Calling_Conventions


System Calls
------------
There are different ways to make system calls between x86 and x64. Additionally,
the constants for the system calls are almost, but not quite, the same between
linux and OSX. See the examples I have, but at least one of them has to
pad the system call identifier with some constant.

I tend to prefer linking the C runtime & standard library and using those
instead of raw system calls. Makes for faster coding of the parts I actually
care about. The downside is that I have to figure out how deal with calling
conventions when 

Extern and Global
-----------------
Global is way of making labels in a assembly program visible outside of that
program. 

Extern operates pretty much the same as in C programs. It tells the assembler
that a symbol will have a definition provided elsewhere.


OS X Quirks
-----------
Getting assembly to work on OS X has some quirks. Both of these pages
have examples that work on OS X

http://cs.lmu.edu/~ray/notes/nasmtutorial/
https://lord.io/blog/2014/assembly-on-osx/


Other Links
-----------
Some simple refresher examples: http://ian.seyler.me/easy_x86-64/
Example of x87 fpu code: https://en.wikibooks.org/wiki/X86_Assembly/Floating_Point
(But don't use x87 unless you have to)
I already linked to this in OSX, but it's a really amazing general resource
for x86-64 programming in NASM: http://cs.lmu.edu/~ray/notes/nasmtutorial/

Wikibook w/ some x86 instructions and examples: 
https://en.wikibooks.org/wiki/X86_Assembly

This has some great gotchas: http://nickdesaulniers.github.io/blog/2014/04/18/lets-write-some-x86-64/
