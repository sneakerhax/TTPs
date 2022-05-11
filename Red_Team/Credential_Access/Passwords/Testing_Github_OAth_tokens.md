# Testing Github OAuth tokens

**Description:** This entry describes how to test discovered Github OAuth tokens

**Mitre Att&ck:** https://attack.mitre.org/techniques/T1078/

**Requirements:** curl

## Testing the Github OAuth token

```
curl -i -H "Authorization: token <ghp_************************************>" \
    https://api.github.com/user/repos
```

List all available repos for specified token
  
## References
* https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api
* https://docs.github.com/en/rest/repos/repos#list-repositories-for-the-authenticated-user
