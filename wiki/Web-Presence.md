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

## Big 3

### [Google](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/lamp)

I think that's the right link. I couldn't find bare Linux servers.

"We can get \$400 of free credit (for 90 days I think) to play with it if people are interested. I could create the VMs and then setup access so configuration/installation could be." - Jot Powers

- Pre-built versions can be deployed. Estimated cost is \<\$5/month. [Bitnami Mediawiki bundle on Ubuntu](https://console.cloud.google.com/marketplace/product/bitnami-launchpad/mediawiki?project=driven-photon-138123)

### [Amazon](https://aws.amazon.com/lightsail/)

### [Microsoft](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/)

"I don't know how many Azure folks we have but the lab has \$2,500 / year free there too. I can certainly get anyone started but we would need more than one person for the reasons already mentioned" - Eric W

I can't figure out how to get a straight price or HDD size from their interface. - Bob Bushman

## Provider Comparison Table

To try to get comparables, I picked the least expensive 2 GB instance. I run 1 GB instances for my wikis, but I figure HSL will have more load.

Prices are based on month-to-month pricing.

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Provider | VPS Plan | Monthly Price | vCPU Cores | RAM | HDD | Bandwidth | Notes |
| [Aquatis](https://aquatis.host/) | [KVM - 2G](https://aquatis.host/kvm-hosting/) | \$5.00 | 2 Cores | 2 GB | 10 GB SSD | 1 TB | Small Storage, Out of Stock, could not confirm price is month-to-month |
| [Interserver](https://www.interserver.net/) | [VPS 1](https://www.interserver.net/vps/) | \$6.00 | 1 Core | 2 GB | 30 GB SSD | 2 TB | Offers 1-click MediaWiki (though having our own deploy process makes lift & shift easier) |
| [Namecheap](https://www.namecheap.com/hosting/) | [Pulsar](https://www.namecheap.com/hosting/vps/) | \$9.88 | 2 Cores | 2 GB | 40 GB SSD RAID 10 | 1 TB | Phoenix Local, RAID 10 |
| [Amazon Lightsail](https://aws.amazon.com/lightsail/) | [Virtual Server 3](https://aws.amazon.com/lightsail/pricing/) | \$10.00 | 1 Core | 2 GB | 60 GB SSD | 3 TB |  |
| [NDCHost](https://www.ndchost.com/) | [Cloud Server \#2](https://www.ndchost.com/cloud-servers/) | \$10.00 | 1 Cores | 2 GB | 50 GB SSD | 2 TB | [Listed on EFF](https://certbot.eff.org/hosting_providers/) as having full support for CertBot. |
| [Google Cloud](https://console.cloud.google.com/) | [LAMP Stack](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/lamp) | \$12.70 | 1 Core | 2 GB | 10 GB | ?? | Small Storage, offers 1-click Bitnami Mediawiki, price is for LAMP - bare Linux instances are \$25.95 |
| [Hostinger](https://www.hostinger.com/) | [VPS2](https://www.hostinger.com/vps-hosting) | \$12.99 | 2 Cores | 2 GB | 40 GB SSD | 2 TB | Europe-based (Lithuania) |
| [Spry](https://www.spryservers.net/) | [SSD KVM Milli](https://www.spryservers.net/vps) | \$20.00 | 2 Cores | 2 GB | 40 GB SSD | ?? |  |
