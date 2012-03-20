## Overview

IT is organized and managed by the [Operations team](Operations-team), primarily Will Bradley and Ryan Rix. Our network is a pretty standard network, all things considered, with a few caveats:

- access to the [dn42](Dn42) hacker darknet
- pfSense routing

## From the Outside

From the outside, hsl-border1 exposes the following ports:

- 22/tcp open ssh
  - forwards to hsl-access:22
- 53/tcp open domain
  - DNS running on hsl-border1
- 80/tcp open http
  - forwards to hsl1:80
- 81/tcp open hosts2-ns
  - forwards to hsl-access.hsl.dn42:81
- 179/tcp open bgp
  - bgp running on hsl-border1 for [dn42](Dn42)
- 443/tcp open https
  - hsl-border1 pfSense administration interface
- 1999/tcp open tcp-id-port
  - ssh access to hsl-boreder1
- 2601/tcp open zebra
  - zebra for dn42 running on hsl-border1
- 2605/tcp open bgpd
  - bgp control daemon running on hsl-border1
- 9000/tcp open cslistener
  - forwards to 172.22.110.11:80
- 9001/tcp open tor-orport
  - forwards to 172.22.110.12:80
- 9002/tcp open dynamid
  - forwards to 172.22.110.13:80 (inactive)

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

#### Overview

This is one of the two IP cameras in the space.

#### Responsible For

- Front of lab security coverage
- Front of lab live.heatsynclabs.org coverage

#### Responsible Parties

- Will Bradley

#### NMAP

     
    [rrix@stinkpad ~]$ nmap 172.22.110.11 -p1-65365

    Starting Nmap 5.51 ( http://nmap.org ) at 2011-12-18 18:51 MST
    Nmap scan report for 172.22.110.11
    Host is up (0.0079s latency).
    Not shown: 65364 closed ports
    PORT   STATE SERVICE
    80/tcp open  http

    Nmap done: 1 IP address (1 host up) scanned in 305.68 seconds

### 172.22.110.12

#### Overview

This is one of the two IP cameras in the space.

#### Responsible For

- Back of lab security coverage
- Back of lab live.heatsynclabs.org coverage

#### Responsible Parties

- Will Bradley

#### NMAP

     
    [rrix@stinkpad ~]$ nmap 172.22.110.12 -p1-65365

    Starting Nmap 5.51 ( http://nmap.org ) at 2011-12-18 18:51 MST
    Nmap scan report for 172.22.110.12
    Host is up (0.0079s latency).
    Not shown: 65364 closed ports
    PORT   STATE SERVICE
    80/tcp open  http

    Nmap done: 1 IP address (1 host up) scanned in 305.68 seconds

### intranet.heatsynclabs.org (172.22.110.15)

#### Overview

intranet.hsl.dn42 provides the heart of our infrastructure system. Responsible for managing access to the 23b [Open Access Control](Open-Access-Control) board which manages our door locks via port 80. This machine also hosts the UniFi control software which manages the wireless APs on our network.

#### Responsible For

- OAC web access
- Ubiquity Wireless AP controls
- SpaceAPI

#### Responsible Parties

- IT
  - Will
  - Ryan

#### NMAP

    [rrix@stinkpad ~]$ nmap 172.22.110.15 -p1-65365

    Starting Nmap 5.51 ( http://nmap.org ) at 2011-12-18 18:59 MST
    Nmap scan report for intranet.heatsynclabs.org (172.22.110.15)
    Host is up (0.010s latency).
    Not shown: 65359 closed ports
    PORT     STATE SERVICE
    22/tcp   open  ssh
    80/tcp   open  http
    8080/tcp open  http-proxy
    8443/tcp open  https-alt
    8843/tcp open  unknown
    8880/tcp open  cddbp-alt

### 172.22.110.16

#### Overview

.16 is the server responsible for serving our main web presences of heatsynclabs.org and wiki.heatsynclabs.org.

#### Responsible For

- Main web content
  - www.heatsynclabs.org
  - toolshare.heatsynclabs.org
  - wiki.heatsynclabs.org
  - mustacheparty.org

#### Responsible Parties

- IT
  - Will (primary)
  - Ryan (has root access)

#### NMAP

    did not run:

    *:80 for http
    *:9393 for ssh

### 172.22.111.240

#### Overview

Fletch's laptop, added a static DHCP reservation for him per request, to aid.

#### Responsible For

- Has port 15900 open on WAN to VNC port on .240 so that Fletch can have remote VNC

#### Responsible Parties

- Fletcher Fowler

#### NMAP

    Not a lab machine, did not run.

### 172.22.111.241

#### Overview

Fletch's laptop, added a static DHCP reservation for him per request, to aid.

#### Responsible For

- Has port 15901 open on WAN to VNC port on .241 so that Bob can have remote VNC

#### Responsible Parties

- Fletcher Fowler

#### NMAP

    Not a lab machine, did not run.

### 172.22.111.242

#### Overview

Fletch's laptop, added a static DHCP reservation for him per request, to aid.

#### Responsible For

- Has port 15902 open on WAN to VNC port on .242 so that Fletch can have remote VNC

#### Responsible Parties

- Fletcher Fowler

#### NMAP

    Not a lab machine, did not run.

### 172.22.111.243

#### Overview

Steve Young's laptop, added a static DHCP reservation for him per request, to aid.

#### Responsible For

- Has port 15903 open on WAN to VNC port on .242 so that Fletch can have remote VNC

#### Responsible Parties

- Steve Young

#### NMAP

    Not a lab machine, did not run.
