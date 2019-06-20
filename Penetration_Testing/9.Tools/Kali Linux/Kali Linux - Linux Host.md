# Kali Linux - Linux Host

**Choose a version of Debian Linux Including one found on a cloud service**

### Adding the Kali Linux sources

Open the sources list by doing the following:

```vim /etc/apt/sources.lst```

Add the sources that can be found [here](http://docs.kali.org/general-use/kali-linux-sources-list-repositories)

### Installing the Kali Linux Metapackages

Run the following to get the list of Kali Linux metapackages:

```apt-get update && apt-cache search kali-linux```

Choose the package that you want to use. I usually choose kali-linux-full

```apt-get install kali-linux-full```

More information can be found [here](https://www.kali.org/news/kali-linux-metapackages/)

### Conclusion

Once you are done you should have all the packages loaded from the metapackage you chose and can use it as you normally would a Kali Linux machine.

