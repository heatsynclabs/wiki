This is intended to document how to install MedaiWiki on Lightsail. It's starting with notes on my attempts and has good intentions to mature into a proper tutorial.

# First Pass: Debian Speedrun

I did a speedrun through the documentation here: <https://www.mediawiki.org/wiki/Manual:Running_MediaWiki_on_Debian_or_Ubuntu>

It works nicely on a \$5 Lightsail box. No load test or anything yet, but it seemed snappy for a few quick page edits.

The tutorial didn't recommend installing Emacs. Clearly an oversight on their part. :D

The tutorial doesn't have Let's Encrypt steps; I want to interject those before the first login.

The MediaWiki tutorial recommends MediaWiki 1.34, the latest stable version. AWS Lightsail Debian is Debian 9.1, which has PHP 7.0. MediaWiki 1.34 requires PHP 7.3. You have to use MediaWiki 1.33 or lower to run on PHP 7.0.

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

I played with the Bitnami LAMP package on Lightsail. It's OK, but the directory structure all starts with /opt/bitnami. All the paths to things like Apache's conf files and the web root path are under /opt/bitnami, and the relative directory structure is non-standard. Using this package as a base means writing a guide that is coupled to Bitnami.

So I looked up the company to see if I trust them. They were a little independent company, they got bought out by VMWare. VMWare is owned by Dell. I don't have a particular problem with Dell, but I don't see the upside in coupling to them to save a few apt install commands.

# Third Pass: Debian 10.5

This time around I'm going with a bare Debian 10.5 instance. I used 9.5 for the first pass, it only has PHP 7.0, which the latest version of MediaWiki won't run on. Debian 10.5 (which I don't recall seeing last time, I think it's new to Lightsail) comes with PHP 7.3, which will support the most current MediaWiki.

I used the \$5 instance with 1 GB RAM, 1 vcPU, 40 GB SSD, and 2 TB transfer. It's the best price/performance they offer at the moment; as you go to larger instances the price grows faster than the specs. If it can run on a \$5 instance, I think it's the right call.

## Static IP Address

Wait for the Lightsail console to show that the instance is "Running" - it should only take a minute or two. Once the instance is up, assign it a static IP address. In the Lightsail console page on AWS, select your instance, and click on the Networking folder tab. Click on "Create Static IP". It will attach an IP from its pool to your instance, and you'll use that IP address for the DNS entries below.

While you're at the Networking configuration, go to the Firewall section and add an entry for 443 (HTTPS).

## OS Updates

Once it's fired up, login and update the OS:

    $ ssh -i <path/to/secret_ssh_key> admin@<ip_address>
    $ sudo apt update
    $ sudo apt dist-upgrade

## DNS Entries

Add A records for each of the hostnames you want to create certificates for. I'm setting up traxel.com, www.traxel.com, and wiki.traxel.com, so I created 3 A Records all pointing to the same static IP address.

Now wait for those records to cascade. It should be done in a day or two.

## Apache

Let's Encrypt creates files on your webserver, then hits the host with an HTTP request to confirm that you own the domain. Install Apache 2 so you can host the files.

    $ sudo apt install apache2

Then you'll need a file like /etc/apache2/sites-available/003-wiki.conf for each of the hostnames. I pointed each one at a different directory, since I don't know if Let's Encrypt uses unique filenames. It probably does, but this guarantees it will work.

    <VirtualHost *:80>
        ServerName wiki.traxel.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/mediawiki

        ErrorLog ${APACHE_LOG_DIR}/wiki-error.log
        CustomLog ${APACHE_LOG_DIR}/wiki-access.log combined
    </VirtualHost>

After you create the conf files, activate them with a2ensite and disable 000-default with a2dissite (unless you're keeping that one active to cover the root hostname).

    $ sudo a2ensite 001-root
    $ sudo a2ensite 002-www
    $ sudo a2ensite 003-wiki
    $ sudo a2dissite 000-default
    $ sudo systemctl reload apache2

Finally we'll need mod_rewrite - Let's Encrypt will create conf files that will redirect non-SSL traffic to HTTPS.

    $ sudo a2enmod rewrite
    $ sudo systemctl restart apache2

## Let's Encrypt SSL Certificate

Let's Encrypt will look at your active sites and ask you if you want to create certs for all of them.

Following this tutorial: <https://www.rosehosting.com/blog/how-to-install-lets-encrypt-on-ubuntu-20-04-with-apache/>

    $ sudo apt install certbot python3-certbot-apache
    $ sudo certbot --apache

Wow! OK, that was way easier than I was expecting. Sure, there's the setup that you have to do, but most of that would have to be done anyway just to get the webserver up. That is really awesome. I'll have to give the EFF a little extra this year.

## MediaWiki Supporting Software

First, the basics. You'll need all of these:

    $ sudo apt-get install mariadb-server php php-mysql libapache2-mod-php php-xml php-mbstring

Next, the enhancements. These will give MediaWiki extra capabilities. See [Optional Packages](https://www.mediawiki.org/wiki/Manual:Running_MediaWiki_on_Debian_or_Ubuntu#Optional_useful_packages)

    $ sudo apt-get install php-apcu php-intl imagemagick php-cli php-curl git

## Configure MariaDB

It's time to stop generically referring to MariaDB as MySQL. MySQL is a once-great project that is no longer trustworthy. MariaDB is the leading Open Source RDBMS.

If you haven't done anything with it yet, there will be no password.

    $ sudo mariadb -u root

Pick a username for MediaWiki to use (I'm using wiki_wiki as an example).

Pick a database name (I'm using hsl_wiki as an example).

Pick a password other than "CHANGE THIS PASSWORD".

    MariaDB> create database hsl_wiki;
    MariaDB> grant all on hsl_wiki.* to 'wiki_wiki'@'localhost' identified by 'CHANGE THIS PASSWORD';
    MariaDB> flush privileges;

Then you can verify it worked if you like. (there won't be any tables, but it shouldn't give you an auth error)

    $ mariadb -u wiki_wiki -p
    MariaDB> show tables in hsl_wiki;
    MariaDB> exit

## MediaWiki

    $ cd
    $ mkdir tmp
    $ cd tmp
    $ wget https://releases.wikimedia.org/mediawiki/1.35/mediawiki-1.35.0.tar.gz
    $ tar -xvzf mediawiki-1.35.0.tar.gz
    $ mv mediawiki-1.35.0 /var/www/

---
*Categories: [Sysadmin Tutorials](Category-Sysadmin-Tutorials)*
