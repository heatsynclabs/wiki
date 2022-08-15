# Social Media

- tbd: link to FB
- tbd: link to Twitter
- tbd: link to ...

# Video Conferencing

## [Jitsi](https://meet.jit.si/) (current solution)

# Real-Time Chat

## [Slack](https://app.slack.com/) (current solution)

- For us limiting the slack to 250/under overall users would be against our mission.
- Slack has been a great tool for us, and pretty dang reliable
- It's not a replacement for Google Groups
- I don't know if Discord would be a replacement for Slack
- If we had to pay for Slack it would not be worth it to our organization
- The more social platforms we have the more fractured the memberbase becomes

### Big Features

### Drawbacks

- 3 months of slack history (regardless of the 10,000 message count)

### Pricing

- if we have less then 250 members, the slack instance would be free
- “weekly active members” seems to be around the 40-55 range
- Looks like slack doesn’t charge for “inactive” members. <https://slack.com/help/articles/218915077-Slacks-Fair-Billing-Policy>
- their regular price after the increase would be around \$4350 per year, or \$652.50 ... \$55 a month basically ... (for 50 users)
- “Pro Plan: We offer workspaces with 250 or fewer members a free upgrade, and an 85% discount for workspaces above that size.” \[ed: for non-profits\]

## [Element.io](https://element.io/)

- Jitsi Integration
- End-to-End Encryption

## [Discord](https://discord.com/)

- "I will say Discord's own tos and coc is kind of a dumpster fire..." (seen on our Slack)

# Discussion Forum

## Google Groups (current solution)

### Big Features

- Bi-Directional Email Sync

### Drawbacks

- Q: Do we have limited retention on Google Groups, like Slack?
- A: No. (to the best of my knowledge. -Jot)

# Calendar

# Wiki

## Current

MediaWiki 1.19 (ca 2012)

## Coming Soon

"I've threatened to upgrade before, but this time I mean it!" - Bob Bushman, Summer 2022

- Bob's first pass, from long ago: [MediaWiki_On_Lightsail](MediaWiki-On-Lightsail)
- More recent pass by Bob, on his own stuff: [MediaWiki Install](https://wiki.traxel.com/index.php/MediaWiki_Install)
- Bob's current attempt: [MediaWiki on Namecheap](https://wiki.traxel.com/index.php/MediaWiki_on_Namecheap)

# Office Suite

## Current

Google Docs

### Big Features

- Integration with Google Groups and Google Calendar.

## Alternatives

### Collabora

#### What's Better

#### What's Worse

# Cloud Hosting Provider

"I suggest that anything hosted in the cloud NOT be created/hosted under an individual’s account. A HSL owned account should be created and everything placed under that." - Jeff Sittler

"I prefer not to run images. If we use our own deploy process we are free to lift and shift to another provider." - Bob Bushman

## Big 3

### [Google](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/lamp)

I think that's the right link. I couldn't find bare Linux servers.

"We can get \$400 of free credit (for 90 days I think) to play with it if people are interested. I could create the VMs and then setup access so configuration/installation could be." - Jot Powers

- Pre-built versions can be deployed. Estimated cost is \<\$5/month. [Bitnami Mediawiki bundle on Ubuntu](https://console.cloud.google.com/marketplace/product/bitnami-launchpad/mediawiki?project=driven-photon-138123)

### [Amazon](https://aws.amazon.com/lightsail/)

### [Microsoft](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/)

"I don't know how many Azure folks we have but the lab has \$2,500 / year free there too. I can certainly get anyone started but we would need more than one person for the reasons already mentioned" - Eric W

I can't figure out how to get a straight price or HDD size for bare Linux instances from their interface. - Bob Bushman

## Provider Comparison Table

To try to get comparables, I picked the least expensive 2 GB instance. I run 1 GB instances for my wikis, but I figure HSL will have more load.

Prices are based on month-to-month pricing.

"To me, Namecheap is the right choice because they are local, use RAID 10, and because of their principles. I already use them for DNS, and as a result of this dive into their principles, I'm going to start shifting my personal hosting there." - Bob Bushman

<table>
<tbody>
<tr>
<td><p>Provider</p></td>
<td><p>VPS Plan</p></td>
<td><p>Monthly Price</p></td>
<td><p>vCPU Cores</p></td>
<td><p>RAM</p></td>
<td><p>HDD</p></td>
<td><p>Data Xfer per Month</p></td>
<td><p>Notes</p></td>
</tr>
<tr>
<td><p><a href="https://aquatis.host/">Aquatis</a></p></td>
<td><p><a href="https://aquatis.host/kvm-hosting/">KVM - 2G</a></p></td>
<td><p>$5.00</p></td>
<td><p>2 Cores</p></td>
<td><p>2 GB</p></td>
<td><p>10 GB SSD</p></td>
<td><p>1 TB</p></td>
<td><p>Small Storage, Out of Stock, could not confirm price is month-to-month</p></td>
</tr>
<tr>
<td><p><a href="https://www.interserver.net/">Interserver</a></p></td>
<td><p><a href="https://www.interserver.net/vps/">VPS 1</a></p></td>
<td><p>$6.00</p></td>
<td><p>1 Core</p></td>
<td><p>2 GB</p></td>
<td><p>30 GB SSD</p></td>
<td><p>2 TB</p></td>
<td><p>Offers 1-click MediaWiki (though having our own deploy process makes lift &amp; shift easier)</p></td>
</tr>
<tr>
<td><p><a href="https://www.namecheap.com/hosting/">Namecheap</a></p></td>
<td><p><a href="https://www.namecheap.com/hosting/vps/">Pulsar</a></p></td>
<td><p>$9.88</p></td>
<td><p>2 Cores</p></td>
<td><p>2 GB</p></td>
<td><p>40 GB SSD RAID 10</p></td>
<td><p>1 TB</p></td>
<td><p>Phoenix Local, RAID 10, <a href="https://www.namecheap.com/about/press-releases/press-releases-info/17-07-04/namecheap_joins_the_battle_for_the_net_protest_on_july_12/">Supports Net Neutrality</a>, <a href="https://www.namecheap.com/about/press-releases/22-03-15/joint-statement">Fought Facebook (and settled)</a>, <a href="https://www.namecheap.com/about/press-releases/22-03-02/free-anonymous-domain-registration-in-russia-belarus">Opposes Invasion of Ukraine</a>, <a href="https://www.namecheap.com/about/press-releases/22-03-15/solopreneurs-savings-web-products">Supports Solo Entrepreneurs and Women Entrepreneurs</a> <a href="https://www.namecheap.com/blog/move-your-domain-day-chat-eff-namecheap/">Supports EFF</a>, <a href="https://www.namecheap.com/blog/namecheap-champions-privacy-standards/">Supports Privacy</a></p>
<p>Turns out their VPS hosting is backed by Amazon AWS. That pretty much blows the "do business with small local businesses" argument.</p></td>
</tr>
<tr>
<td><p><a href="https://aws.amazon.com/lightsail/">Amazon Lightsail</a></p></td>
<td><p><a href="https://aws.amazon.com/lightsail/pricing/">Virtual Server 3</a></p></td>
<td><p>$10.00</p></td>
<td><p>1 Core</p></td>
<td><p>2 GB</p></td>
<td><p>60 GB SSD</p></td>
<td><p>3 TB</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="https://www.ndchost.com/">NDCHost</a></p></td>
<td><p><a href="https://www.ndchost.com/cloud-servers/">Cloud Server #2</a></p></td>
<td><p>$10.00</p></td>
<td><p>1 Cores</p></td>
<td><p>2 GB</p></td>
<td><p>50 GB SSD</p></td>
<td><p>2 TB</p></td>
<td><p><a href="https://certbot.eff.org/hosting_providers/">Listed on EFF</a> as having full support for CertBot.</p></td>
</tr>
<tr>
<td><p><a href="https://console.cloud.google.com/">Google Cloud</a></p></td>
<td><p><a href="https://console.cloud.google.com/marketplace/details/click-to-deploy-images/lamp">LAMP Stack</a></p></td>
<td><p>$12.70</p></td>
<td><p>1 Core</p></td>
<td><p>2 GB</p></td>
<td><p>10 GB</p></td>
<td><p>??</p></td>
<td><p>Small Storage, offers 1-click Bitnami Mediawiki, price is for LAMP - bare Linux instances are $25.95</p></td>
</tr>
<tr>
<td><p><a href="https://www.hostinger.com/">Hostinger</a></p></td>
<td><p><a href="https://www.hostinger.com/vps-hosting">VPS2</a></p></td>
<td><p>$12.99</p></td>
<td><p>2 Cores</p></td>
<td><p>2 GB</p></td>
<td><p>40 GB SSD</p></td>
<td><p>2 TB</p></td>
<td><p>Europe-based (Lithuania)</p></td>
</tr>
<tr>
<td><p><a href="https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/">Microsoft</a></p></td>
<td><p><a href="https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/">Linux VM B1ms</a></p></td>
<td><p>$15.11</p></td>
<td><p>1 Core</p></td>
<td><p>2 GB</p></td>
<td><p>??</p></td>
<td><p>??</p></td>
<td><p>I cannot find what 4 GiB of "Temporary Storage" is, how much HDD space it comes with, nor how much data transfer is included. But supposedly we get $2500/year for free (since we're a 501c3? ref: Jot Powers)</p></td>
</tr>
<tr>
<td><p><a href="https://www.spryservers.net/">Spry</a></p></td>
<td><p><a href="https://www.spryservers.net/vps">SSD KVM Milli</a></p></td>
<td><p>$20.00</p></td>
<td><p>2 Cores</p></td>
<td><p>2 GB</p></td>
<td><p>40 GB SSD</p></td>
<td><p>??</p></td>
<td></td>
</tr>
</tbody>
</table>
