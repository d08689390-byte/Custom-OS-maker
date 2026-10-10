; Multiboot header constants
MODULEALIGN equ 1 << 0
MEMINFO     equ 1 << 1
FLAGS       equ MODULEALIGN | MEMINFO
MAGIC       equ 0x1BADB002
CHECKSUM    equ -(MAGIC + FLAGS)

section .multiboot
align 4
    dd MAGIC
    dd FLAGS
    dd CHECKSUM

section .text
global _start
extern kernel_main

_start:
    mov esp, stack_space        ; Set up stack pointer
    call kernel_main
    cli
.hang:
    hlt
    jmp .hang

section .bss
resb 8192                       ; 8KB memory area for stack
stack_space:
