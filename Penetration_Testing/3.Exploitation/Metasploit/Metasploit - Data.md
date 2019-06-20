# Metasploit - Data

```db_connect msf@msf4```

Connecting to Metasploit database

```db_connect --token <token> --cert <pem_file> --skip-verify https://localhost:5443```

Connecting to web service from framework ([wiki](https://github.com/rapid7/metasploit-framework/wiki/Metasploit-Web-Service))

```msfdb --component webservice --address 0.0.0.0 start```

Starting web service

```msfdb --component webservice stop```

Stopping web service

```db_disconnect```

Disconnect from data source
