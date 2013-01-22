BigBlueButton is a video conferencing server. It is built on a collection of FLOSS projects including FreeSWITCH, which also gives it the ability to route SIP calls, giving users the ability to do text chat, VoIP, and video chat with end to end encryption.

I am attempting to get all the pieces working on a personal server and on a machine at HSL. I have built up a fair bit of state, and I'm figuring to use this page for notes so I don't lose my place. Perhaps it will also act as breadcrumbs for future explorers if my attempt goes pear-shaped. :)

# FreeSWITCH, Jitsi, ZRTP

FreeSWITCH is a component of BigBlueButton that routes SIP calls. I have it installed and routing calls between softphones, but I do not have everything working yet. I have not made a successful SIP call between two different clients, I do not have video working through FreeSWITCH (though direct dialing with Jitsi works), and I do not have ZRTP working through FreeSWITCH (again, working with direct Jitsi-to-Jitsi calls).

I have just grabbed the Jitsi source code, wiped my installs, and re-verified that direct Jitsi-to-Jitsi calls have encryption and video. Now I am going to document the failures and see if I can find any useful info in the logs. Jitsi logs are pretty sparse, even with debug enabled, so I may wind up adding log statements.

## Jitsi-to-Jitsi, Direct Connect, ZRTP+Video

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

## Jitsi-to-Jitsi, Via FreeSWITCH, fail ZRTP and Video

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

## Possible Solution: FreeSWITCH: Proxy Media

<http://wiki.freeswitch.org/wiki/Proxy_Media>

Looking like a promising path. Proxy Media basically means, "Hey, FreeSWITCH: You're just a dumb router, not a valued participant in my telephone call."

I now have made video calls from Linphone/Linux to Linphone/Cyanogenmod, and have some promising looking ZRTP (encryption) error messages connecting from Jitsi/Linux to Jitsi/OS-X.

Probably no more progress for a few days, business trip.
