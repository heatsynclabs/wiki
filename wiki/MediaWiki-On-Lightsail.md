This is intended to document how to install MedaiWiki on Lightsail. It's starting with notes on my attempts and has good intentions to mature into a proper tutorial.

# First Pass: Debian Speedrun

I did a speedrun through the documentation here: <https://www.mediawiki.org/wiki/Manual:Running_MediaWiki_on_Debian_or_Ubuntu>

It works nicely on a \$5 Lightsail box. No load test or anything yet, but it seemed snappy for a few quick page edits.

The tutorial didn't recommend installing Emacs. Clearly an oversight on their part. :D

The tutorial doesn't have Let's Encrypt steps; I want to interject those before the first login.

The MediaWiki tutorial recommends MediaWiki 1.34, the latest stable version. AWS Lightsail Debian is Debian 9.1, which has PHP 7.0. MediaWiki 1.34 requires PHP 7.3 (I think). You have to use MediaWiki 1.33 or lower to run on PHP 7.0.

# To Do

- Document Lightsail Setup
  - Port Restrictions
  - SSH Login Key
  - Distro
    - Try out the "Apps + OS" Bitnami LAMP PHP 7.x instance.
- Let's Encrypt
- Backup and Restore
  - Database Dump and Import
  - LocalSettings.php backup and import
  - Periodic Backup

# Second Pass: Bitnami LAMP

- It comes with phpMyAdmin - is that a plus, minus, or indifferent?

---
*Categories: [Sysadmin Tutorials](Category-Sysadmin-Tutorials)*
