# Powershell Remoting

**Description:** This entry describes how to use Powershell Remoting for lateral movement

**Requirements:** powershell

## Running remote commands with Powershell Remoting

```
$cred = Get-Credential
```

Setting up credentials (prompt will come up for creds)

```
$session = New-PSSession
```

Setting up session

```
Enter-PSSession $session
```

Entering the session
  
## References
* [MSLearn - Running Remote Commands](https://learn.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands)