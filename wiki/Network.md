## Active Systems

### hsl-border1.hsl.dn42 (172.22.110.1)

#### Overview

.1 is hsl-border1.hsl.dn42, our main router and gateway to the wide world of the internet. This machine serves as our connection to the OneAxis PPP setup as well as the [dn42](Dn42) darknet.

The machine is a pfSense box running upstairs, labelled hsl-firewall

#### Responsible For

- Routing
- Gateway to internet
- Gateway to dn42

#### Responsible Parties

- IT
  - Will
  - Ryan

#### NMAP

    [rrix@stinkpad ~]$ nmap hsl-border1.hsl.dn42 -p1-65365

    Starting Nmap 5.51 ( http://nmap.org ) at 2011-12-18 18:43 MST
    Nmap scan report for hsl-border1.hsl.dn42 (172.22.110.1)
    Host is up (0.011s latency).
    Not shown: 65358 filtered ports
    PORT     STATE SERVICE
    53/tcp   open  domain
    80/tcp   open  http
    179/tcp  open  bgp
    443/tcp  open  https
    1999/tcp open  tcp-id-port
    2601/tcp open  zebra
    2605/tcp open  bgpd

    Nmap done: 1 IP address (1 host up) scanned in 240.43 seconds

### 172.22.110.11

### 172.22.110.12

### intranet.heatsynclabs.org (172.22.110.15)

Nmap scan report for 172.22.110.16
