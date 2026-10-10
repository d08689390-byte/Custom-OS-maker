void kernel_main(void) {
    const char *str = "Hello from Codespaces!";
    char *vidptr = (char*)0xb8000; // Video memory addresses begin here
    unsigned int i = 0;
    unsigned int j = 0;

    // Clear the screen (25 lines of 80 columns)
    while(j < 80 * 25 * 2) {
        vidptr[j] = ' ';
        vidptr[j+1] = 0x07; // Light grey attribute
        j = j + 2;
    }

    j = 0;
    // Write the string to video memory
    while(str[i] != '\0') {
        vidptr[j] = str[i];
        vidptr[j+1] = 0x07; // Attribute byte: text color
        i++;
        j = j + 2;
    }
    return;
}
