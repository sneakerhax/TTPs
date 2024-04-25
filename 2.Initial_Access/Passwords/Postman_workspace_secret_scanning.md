# Postman workspace secret scanning

**Description:** This entry describes how to scan for secrets in public Postman workspaces using Trufflehog

**Requirements:** trufflehog

## Discovering public Postman workspaces

```
https://www.postman.com/search?q=<search_term>&scope=all&type=workspace
```

Add the search term to the query and paste it into a browser. Use the reference "How to find the ID of an element in Postman" to discover the Workspace ID.

## Using Trufflehog to search public Postman workspaces for secrets

```
trufflehog postman --workspace <workspace_id> --token <postman_api_token>
```

Add the workspace ID discovered above and your Postman API token.
  
## References
* [(The) Postman Carries Lots of Secrets](https://trufflesecurity.com/blog/postman-carries-lots-of-secrets)
* [How to find the ID of an element in Postman](https://support.postman.com/hc/en-us/articles/5063785095319-How-to-find-the-ID-of-an-element-in-Postman)
* [Generate and use Postman API keys](https://learning.postman.com/docs/developer/postman-api/authentication/)
