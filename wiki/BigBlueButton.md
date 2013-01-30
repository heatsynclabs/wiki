BigBlueButton is a video conferencing server. It is built on a collection of FLOSS projects including FreeSWITCH, which also gives it the ability to route SIP calls and XMPP sessions, giving users the ability to do text chat, VoIP, and video chat with end to end encryption.

I am attempting to get all the pieces working on a personal server and on a machine at HSL. I have built up a fair bit of state, and I'm figuring to use this page for notes so I don't lose my place. Perhaps it will also act as breadcrumbs for future explorers if my attempt goes pear-shaped. :)

# SIP

## FreeSWITCH, Jitsi, ZRTP

FreeSWITCH is a SIP router that is bundled with BigBlueButton. I have it installed and routing calls between softphones, but I do not have everything working yet. I have not made a successful SIP call between two different clients, I do not have video working through FreeSWITCH (though direct dialing with Jitsi works), and I do not have ZRTP working through FreeSWITCH (again, working with direct Jitsi-to-Jitsi calls).

I have just grabbed the Jitsi source code, wiped my installs, and re-verified that direct Jitsi-to-Jitsi calls have encryption and video. Now I am going to document the failures and see if I can find any useful info in the logs. Jitsi logs are pretty sparse, even with debug enabled, so I may wind up adding log statements.

### Jitsi-to-Jitsi, Direct Connect, ZRTP+Video

    Call information :
     Identity : bob (RegistrarLess SIP)
     bob@192.168.1.10 :
     Call duration : 00:22:29
     Audio info :
     Media stream transport protocol : UDP / SRTP (Key exchange protocol: ZRTP AES-CM-128/DH3K)
     Codec / Frequency : opus / 48000 Hz
     Local IP / Port : 192.168.1.6 / 5000
     Remote IP / Port : 192.168.1.10 / 5000
     Bandwith : ↓ 6 Kbps ↑ 28 Kbps
     Loss rate : ↓ 0% ↑ 0%
     Packets decoded with FEC : 1
     Packets currently being discarded : 0%
     Number of discarded packets : 2 (0 late, 1 full, 0 shrink, 1 reset)
     Adaptive jitter buffer : enabled
     Jitter buffer : ~40ms;
     currently in queue: 1/4 packets
     RTT : 7 ms
     Jitter : ↓ 2 ms ↑ 0 ms
     Video info :
     Media stream transport protocol : UDP / SRTP (Key exchange protocol: ZRTP AES-CM-128)
     Video size : ↓ 640 x 480 ↑ 640 x 480
     Codec / Frequency : H264 / 90000 Hz
     Local IP / Port : 192.168.1.6 / 5002
     Remote IP / Port : 192.168.1.10 / 5002
     Bandwith : ↓ 35 Kbps ↑ 46 Kbps
     Loss rate : ↓ 0% ↑ 0%
     Packets decoded with FEC : 0
     Packets currently being discarded : 0%
     Number of discarded packets : 0 (0 late, 0 full, 0 shrink, 0 reset)
     Adaptive jitter buffer : enabled
     Jitter buffer : ~100ms;
     currently in queue: 0/11 packets
     RTT : 396 ms
     Jitter : ↓ 2 ms ↑ 3 ms

### Jitsi-to-Jitsi, Via FreeSWITCH, fail ZRTP and Video

    Call information :
     Identity : 1003@192.168.1.7 (SIP) Signalling
     call transport : UDP
     
     1004@192.168.1.7 :
     Call duration : 00:01:08

     Audio info :
     Media stream transport protocol : UDP / RTP
     Codec / Frequency : G722 / 16000 Hz
     Local IP / Port : 192.168.1.6 / 5028
     Remote IP / Port : 192.168.1.7 / 31332
     Bandwith : ↓ 68 Kbps ↑ 64 Kbps
     Loss rate : ↓ 0% ↑ 0%
     Packets decoded with FEC : 0
     Packets currently being discarded : 0%
     Number of discarded packets : 7 (0 late, 7 full, 0 shrink, 0 reset)
     Adaptive jitter buffer : enabled
     Jitter buffer : ~40ms;
     currently in queue: 0/4 packets
     Jitter : ↓ 1 ms ↑ 0 ms 

### Possible Solution: FreeSWITCH: Proxy Media

<http://wiki.freeswitch.org/wiki/Proxy_Media>

Looking like a promising path. Proxy Media basically means, "Hey, FreeSWITCH: You're just a dumb router, not a trusted participant in my telephone call."

I now have made video calls from Linphone/Linux to Linphone/Cyanogenmod, and have some promising looking ZRTP (encryption) error messages connecting from Jitsi/Linux to Jitsi/OS-X.

### Post-Linphone Jitsi Testing

#### Jitsi-to-Jitsi Direct

Testing with jitsi-src-1.1.4412.10296.

1\. Direct dial from Linux to Mac. 2. Initiate video from Linux side. 3. Initiate video from Mac side. 4. Both video working.

1\. Direct dial from Linux to Mac. 2. Initiate video from Mac side. 3. Mac client exits abnormally.

## ZRTP Support Notes

### Linphone

<https://github.com/bitzeppelin/linphone-sdk/blob/master/README.zrtp>

Readme on the inclusion of GNU ZRTP in the Linphone codebase. Includes notes on enabling ZRTP at compile time. Perhaps published binaries do not include ZRTP support? Confirmed -- published binaries do not have ZRTP support.

Compiling with ZRTP support requires at least libzrtpcpp 2.1.2. Debian testing and sid are at 2.0.x. Debian experimental has 2.3.2. After installing libzrtpcpp2_2.3.2 and libzrtpcpp-dev_2.3.2, I finally managed to compile Linphone with ZRTP support. This is not a practical solution for most people. It may help me to validate FreeSWITCH, but as far as end-to-end encrypted comm goes, Linphone is still a work in progress.

# XMPP

XMPP is the Jabber protocol, initially created for text chat. It has been extended to include voice and video with Jingle.

## Text

XMPP was originally designed for text.

## Jingle

Jingle is an extension to XMPP that enables voice, video, and other new features.

## Voice

## Video

## Encryption

ZRTP can be used with XMPP, and I think it has other options for end-to-end encryption.

### ZRTP

## OTR

Off-the-Record Messaging, commonly referred to as OTR, is a cryptographic protocol that provides strong encryption for instant messaging conversations. OTR uses a combination of the AES symmetric-key algorithm, the Diffie–Hellman key exchange, and the SHA-1 hash function. In addition to authentication and encryption, OTR provides perfect forward secrecy and malleable encryption.

<http://wiki.xmpp.org/web/OTR>

# ICE

ICE (Interactive Connectivity Establishment) is a method for negotiating NAT traversal (getting through firewalls) for clients that are using multiple channels. The core spec was designed with SIP in mind, and it now has a parallel spec in XMPP.

<http://en.wikipedia.org/wiki/Interactive_Connectivity_Establishment>

<http://xmpp.org/extensions/xep-0176.html>
