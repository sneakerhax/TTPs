# Docker

Resources related to Docker, building offensive security Tools with Docker, Attacking Docker, and Securing Docker

## General
* [Docker Overview](https://docs.docker.com/engine/docker-overview/) - Docker
* [How Docker Works - Intro to Namespaces](https://youtu.be/-YnMr1lj4Z8) - LiveOverflow
* [Deepdive Containers - Kernel Sources and nsenter](https://youtu.be/sHp0Q3rvamk) - LiveOverflow
* [Container Runtimes Part 1: An Introduction to Container Runtimes](https://www.ianlewis.org/en/container-runtimes-part-1-introduction-container-r) - Ian Lewis
* [Understanding Containerization By Recreating Docker](https://itnext.io/linux-container-from-scratch-339c3ba0411d) - Daniel Mitre
* [Bocker - Docker implemented in around 100 lines of bash](https://github.com/p8952/bocker) - Peter Wilmott
* [Top 20 Dockerfile best practices](https://sysdig.com/blog/dockerfile-best-practices/) - Álvaro Iradier (sysdig)
* [The capable kernel an intro to linux capabilities](https://www.starkandwayne.com/blog/the-capable-kernel-an-introduction-to-linux-capabilities/) - James Hunt
* [Github Actions - Build and push Docker images](https://github.com/marketplace/actions/build-and-push-docker-images) - Docker
* [Container Training](https://container.training/) - Jérôme Petazzoni

## Offensive Docker (Tooling)

* [Docker for Pentesters](https://blog.ropnop.com/docker-for-pentesters/) - ropnop
* [Serverless Toolkit for Pentesters](https://blog.ropnop.com/serverless-toolkit-for-pentesters/) - ropnop
* [Introduction to Docker for CTFs](https://youtu.be/cPGZMt4cJ0I) - LiveOverflow
* [Solving Pwnable CTF Challenge With Docker Workflow](https://youtu.be/OqTpc_ljPYk) - Live Overflow
* [Red Cloud](https://github.com/khast3x/Redcloud) - khast3x

## Vulns and Exploit

* [CVE Details for Docker](https://www.cvedetails.com/vulnerability-list/vendor_id-13534/product_id-28125/Docker-Docker.html) - cvedetails
* [Docker Patched the Most Severe Copy Vulnerability to Date With CVE-2019-14271](https://unit42.paloaltonetworks.com/docker-patched-the-most-severe-copy-vulnerability-to-date-with-cve-2019-14271/) - Yuval Avrahami (Palo Alto Networks)
* [Vulnerabilities in the Container Ecosystem: A Brief History](https://blog.aquasec.com/container-security-vulnerabilities) - aquasec
* [CVE-2020-15275: New Vulnerability Exploits containerd-shim API](https://blog.aquasec.com/cve-2020-15257-containerd-shim-api-vulnerability) - Gal Singer (aquasec)
* [ABSTRACT SHIMMER (CVE-2020-15257): Host Networking is root-Equivalent, Again](https://research.nccgroup.com/2020/12/10/abstract-shimmer-cve-2020-15257-host-networking-is-root-equivalent-again/) - Jeff Dileo (NCC Group)

## Attacking Docker

* [Plundering Docker Images](https://blog.ropnop.com/plundering-docker-images/) - ropnop
* [Attacking Docker exposed API](https://medium.com/@riccardo.ancarani94/attacking-docker-exposed-api-3e01ffc3c124) - Riccardo Ancarani
* [Metasploit - Docker Daemon - Unprotected TCP Socket Exploit](https://www.rapid7.com/db/modules/exploit/linux/http/docker_daemon_tcp/) - Martin Pizala (Rapid7)
* [An Attacker Looks at Docker Approaching Multi Container Applications](https://youtu.be/-Ug2vmRiI8g) - Wesley McGrew
* [Attacking Docker Environments](https://morphuslabs.com/attacking-docker-environments-a703fcad2a39) - Victor Pasknel
(morphuslabs)
* [ippsec.rocks - Type "docker" as the search term](https://ippsec.rocks/) - IppSec
* [Docker image history modification - why you can't trust docker history](https://www.justinsteven.com/posts/2021/02/14/docker-image-history-modification/) - justinsteven
* [Watch Your Containers: Doki Infecting Docker Servers in the Cloud](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/) - Nicole Fishbein and Michael Kajiloti (Intezer)
* [PLAYING WITH NAMESPACES - WRITING DOCKER-AWARE ROOTKITS](https://pulsesecurity.co.nz/articles/docker-rootkits) - Denis Andzakovic (Pulse Security)

## Container Escapes

* [Abusing access to mount namespaces through /proc/pid/root](https://labs.f-secure.com/blog/abusing-the-access-to-mount-namespaces-through-procpidroot/) - Pasi Saarinen (F-Secure)
* [Understanding Docker container escapes](https://blog.trailofbits.com/2019/07/19/understanding-docker-container-escapes/) - Dominik Czarnota (Trail of Bits)
* [A Tale of Escaping a Hardened Docker container](https://www.redtimmy.com/docker/a-tale-of-escaping-a-hardened-docker-container/) - Red Timmy Security
* [The Route to Root: Container Escape Using Kernel Exploitation](https://www.cyberark.com/resources/threat-research-blog/the-route-to-root-container-escape-using-kernel-exploitation) Nimrod Stoler (CyberArk)
* [A Compendium of Container Escapes](https://youtu.be/BQlqita2D2s) ([slides](https://i.blackhat.com/USA-19/Thursday/us-19-Edwards-Compendium-Of-Container-Escapes-up.pdf)) - Brandon Edwards & Nick Freeman
* [Traitor - Automatic Linux privesc via exploitation of low-hanging fruit](https://github.com/liamg/traitor) - liamg
* [Docker - PRIVILEGE ESCALATION Technique](https://youtu.be/MnUtHSpcdLQ) - John Hammond

## Securing Docker

* [Docker Security Docs](https://docs.docker.com/engine/security/security/) - Docker
* [Docker Bench Security](https://github.com/docker/docker-bench-security) - Docker
* [Manage sensitive data with Docker secrets](https://docs.docker.com/engine/swarm/secrets/) - Docker
* [Owasp - Docker Security](https://github.com/OWASP/Docker-Security) - OWASP
* [Owasp - Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) - OWASP
* [10 Docker Image Security Best Practices](https://snyk.io/blog/10-docker-image-security-best-practices/) - Liran Tal and Omer Levi Hevroni (snyk)
* [Docker security scanning cheatsheet 2021](https://snyk.io/blog/docker-security-scanning-cheatsheet-2021/) - Jim Armstrong (snyk)
* [Docker Security 101](https://www.stackrox.com/post/2019/09/docker-security-101/) - Ajmal Kohgadai (StackRox)
* [Docker Security](http://containertutorials.com/docker-security.html) - Rajdeep Dua (Container Tutorials)
* [What security concerns should I have with Docker?](https://github.com/bretfisher/ama/issues/17) - Bret Fisher
* [Understanding and Hardening Linux Containers](https://research.nccgroup.com/wp-content/uploads/2020/07/ncc_group_understanding_hardening_linux_containers-1-1.pdf) - Aaron Grattafior (NCC Group)
* [Dockerizing with Distroless](https://medium.com/@luke_perry_dev/dockerizing-with-distroless-f3b84ae10f3a) - Luke Perry

## Open Source Tools
* [Trivy](https://github.com/aquasecurity/trivy) - aquasecurity
* [Clair](https://github.com/quay/clair) - Quay
* [Anchore](https://github.com/anchore/anchore-engine) - Anchore
* [Dockerscan](https://github.com/cr0hn/dockerscan) - cr0hn
* [Docker_Explorer](https://github.com/matiassequeira/docker_explorer) - matiassequeira
* [SecretScanner](https://github.com/deepfence/SecretScanner) - DeepFence
