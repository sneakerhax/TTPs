# Crunch

**Description:** This entry describes how to generate custom password lists using crunch

**Requirements:** crunch

## Generating custom password lists using crunch

```
crunch 6 6 0123456789ABCDEF -o passwords.txt
```

Generating wordlist with crunch containing the characters 0-9 and A-F 1-6 characters long

```
/usr/share/crunch/charset.lst
```

Pre-defined crunch character sets Kali Linux

```
crunch 4 4 -f /usr/share/crunch/charset.lst mixalpha
```

Using crunch pre-defined character sets(More can be found in the man page)

```
| Character     | Type                               |
| ------------- |:----------------------------------:|
| @             | Lower case alpha characters        |
| ,             | Upper case alpha characters        |
| %             | Numeric characters                 |
| ^             | Special characters including space |
```

Crunch Custom translation placeholders

```
crunch 8 8 -t ,@@^^%%%
```

Generating customer translation wordlist
  
## References
* [Kali Tool - crunch](https://www.kali.org/tools/crunch/)