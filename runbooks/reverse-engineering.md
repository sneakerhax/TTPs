# Reverse Engineering
Notes on reverse engineering

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

## Dynamic Analysis

### Ollydbg

Layout:

<table align="center">
    <tr>
        <td align="center">ASM View</td>
        <td align="center">Registers</td>
    </tr>
    <tr>

        <td align="center">Memory Dump</td>
        <td align="center">Stack Memory</td>
    </tr>
</table>

Useful commands:

```File --> Open --> (Provide arguments into *Arguments* field eg. AAAAAA)```

Load program with arguments

### Immunity Debugger

Layout:

<table align="center">
    <tr>
        <td align="center">ASM View</td>
        <td align="center">Registers</td>
    </tr>
    <tr>

        <td align="center">Memory Dump</td>
        <td align="center">Stack Memory</td>
    </tr>
</table>

Hotkeys:

```
F2 - Set breakpoint
F7 - Step into(step into instruction and run then stop)
F8 - Step over(step over instruction and run next command)
F9 - Start program
```

Letters in menu:

```
e - executable modules
m - memory map
c - cpu view
```

Useful commands:

```right click and choose hex —>> hex/ascii (16 bytes)```

Change to hex 16 bytes view(Hover over memory dump)

```Start program then go to Attach —>> choose running process```

Attach to running process

```Right click register -->> Follow in Dump```

Jump to register in memory dump


