## Static Analysis

```strings <filename>```

prints out all ascii strings found in binary

```file <filename>```

prints out file type information

```hexdump <filename>```

prints hex dump of file

```xxd <filename>```

prints hex dump of file with string data

```xxd -l 4 <filename>```

print magic bytes - List of file signatures([magic bytes](https://en.wikipedia.org/wiki/List_of_file_signatures))

```echo -n "A" | xxd```

Convert ASCII character to hex(-n required to avoid newline)

```echo -n "41" | xxd -r -p```

Convert hex to ASCII

```gobjdump -f <filename>```

print out file headers

```gobjdump -f --section-headers <filename>```

print out file headers and section headers

```gobjdump -x <filename>```

print all file headers

```gobjdump -d <filename>```

print disassembly of file

```ld <filename> ```

print statically linked shared libaries

```strace <filename>```

print all system calls


```ltrace <filename>```

print all library calls

