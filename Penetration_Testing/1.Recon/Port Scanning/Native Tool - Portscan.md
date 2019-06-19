## Scanning

```FOR /L %x in (1,1,255) do ping -n 1 192.168.2.%x | find /I "reply" >> c:\temp\pingresult.txt```

Ping scan from Windows command line

```1..255 | foreach-object { (new-object System.Net.Networkinformation.Ping).Send("192.168.2.$_") } | where-object {$_.Status -eq "success"} | select Address```

Ping scan with Windows Powershell

```for i in {1..254}; do ping -c 1 -W 1 192.168.1.$i | grep 'from'; done```

Ping scan Linux command line

```for p in {443..443}; do(echo >/dev/tcp/*host*/$p) >/dev/null 2>&1 && echo "$p open" || echo "$p closed"; done```

Port scan Linux command line
