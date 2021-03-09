# Reducing the size Golang binaries

```go build -ldflags="-s -w" <file.go>```

Use linker flags to strip debugging information

```upx --brute <binary>```

Pack the binary with UPX

## References
* https://blog.filippo.io/shrink-your-go-binaries-with-this-one-weird-trick/
* https://formulae.brew.sh/formula/upx
