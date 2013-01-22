BigBlueButton is a video conferencing server. It is built on a collection of FLOSS projects including FreeSWITCH, which also gives it the ability to route SIP calls, giving users the ability to do text chat, VoIP, and video chat with end to end encryption.

I am attempting to get all the pieces working on a personal server and on a machine at HSL. I have built up a fair bit of state, and I'm figuring to use this page for notes so I don't lose my place. Perhaps it will also act as breadcrumbs for future explorers if my attempt goes pear-shaped. :)

# FreeSWITCH, Jitsi, ZRTP

FreeSWITCH is a component of BigBlueButton that routes SIP calls. I have it installed and routing calls between softphones, but I do not have everything working yet. I have not made a successful SIP call between two different clients, I do not have video working through FreeSWITCH (though direct dialing with Jitsi works), and I do not have ZRTP working through FreeSWITCH (again, working with direct Jitsi-to-Jitsi calls).

I have just grabbed the Jitsi source code, wiped my installs, and re-verified that direct Jitsi-to-Jitsi calls have encryption and video. Now I am going to document the failures and see if I can find any useful info in the logs. Jitsi logs are pretty sparse, even with debug enabled, so I may wind up adding log statements.
