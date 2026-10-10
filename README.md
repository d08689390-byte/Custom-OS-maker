# Welcome to Custom-OS-maker (Linux Distro)
## Just fork this repo and run this line of code in a codespace,
```
sudo apt update && sudo apt install -y build-essential bison flex libgmp3-dev libmpfr-dev libmpc-dev texinfo qemu-system-x86 grub-pc-bin xorriso
```
### Then edit the boot.asm, linker.ld and kernel.c files to your liking,                                                              
### Then run in the codespace 
```
# Assemble boot.asm
nasm -f elf32 boot.asm -o boot.o

# Compile kernel.c
gcc -m32 -c kernel.c -o kernel.o -std=gnu99 -ffreestanding -O2 -Wall -Wextra

# Link files into a kernel binary
ld -m elf_i386 -T linker.ld -o kernel.bin boot.o kernel.o

# Create a bootable ISO layout
mkdir -p iso/boot/grub
cp kernel.bin iso/boot/

# Create a GRUB configuration file
echo 'set timeout=0' > iso/boot/grub/grub.cfg
echo 'set default=0' >> iso/boot/grub/grub.cfg
echo 'menuentry "My Codespaces OS" {' >> iso/boot/grub/grub.cfg
echo '  multiboot /boot/kernel.bin' >> iso/boot/grub/grub.cfg
echo '}' >> iso/boot/grub/grub.cfg

# Generate the ISO image
grub-mkrescue -o (os name)*.iso iso

```
### * just remember to change (os name) to the os or distro name you would like and thats it! Just run it in a QEMU enviroment and there! You have your own OS!
