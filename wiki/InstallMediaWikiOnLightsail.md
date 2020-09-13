This is intended to document how to install MedaiWiki on Lightsail. It's starting with notes on my attempts and has good intentions to mature into a proper tutorial.

I did a speedrun through the documentation here: <https://www.mediawiki.org/wiki/Manual:Running_MediaWiki_on_Debian_or_Ubuntu>

It works nicely on a \$5 Lightsail box. No load test or anything yet, but it seemed snappy for a few quick page edits.

The tutorial didn't recommend installing Emacs. Clearly an oversight on their part. :D

The tutorial doesn't have Let's Encrypt steps; I want to interject those before the first login.

# To Do

- Document Lightsail Setup
  - Port Restrictions
  - SSH Login Key
  - Distro
- Let's Encrypt
- Backup and Restore
  - Database Dump and Import
  - LocalSettings.php backup and import
  - Periodic Backup

---
*Categories: [Sysadmin Tutorials](Category-Sysadmin-Tutorials)*
