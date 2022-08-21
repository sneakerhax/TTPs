# Reducing the size Golang of binaries

**Description:** This entry describes how to reduce the size of golang binaries that are typically larger in size then other compiled binaries. This is due to the fact that all dependencies are packed into the binary

**Requirements:** upx

## Reducing binary size

```
go build -ldflags="-s -w" <file.go>
```

Use linker flags to strip debugging information

```
upx --brute <binary>
```

Pack the binary with UPX

## References
* https://blog.filippo.io/shrink-your-go-binaries-with-this-one-weird-trick/
* https://formulae.brew.sh/formula/upx
