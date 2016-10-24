#!/bin/bash
gcc -shared -fPIC hello.c -o hello.so
gcc call_hello.c -ldl 
