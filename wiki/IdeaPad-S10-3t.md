So, Intel gave us all these cool netbook tablets. What can we do with them?

## MeeGo Hax

### Its a Linux box, put Linux stuff on it

Zypper is the default package management system for MeeGo. Many standard GNU utilities are included in the default repos. You should install these if you're a developer:

- vim
- gcc
- git
- ruby
- ruby-irb

Searching for packages is fairly straightforward:

    $ zypper search chromium

Installing packages requires root privies, which you can use sudo to gain using the password that was assigned by default (1234):

    $ sudo zypper install chromium

### Make Tablet Less Suck

- Install [chromeTouch](http://www.chromeextensions.org/appearance-functioning/chrometouch/) extension.

### Install KDE

For those of you who don't RAGE RAGE RAGE about KDE, you can install KDE on to MeeGo, including experimental KDEPIM mobile packages, which are freaking sexy.

[installation details](http://userbase.kde.org/Kontact_Touch/MeeGo)

### Make Virtual Keyboard Work

Instructions taken from: [1](http://blog.neteril.org/2010/11/19/turning-your-meego-lenovo-s10-3t-into-a-real-slate/)

1\. To get the keyboard in place.. open the terminal and run these lines.. (The \$ is the command prompt

    $ sudo -s
           (password is 1234 by default)
    $ cd /etc/zypp/repos.d/
    $ sudo -s
    $ cp netbook.repo handset.repo
    $ sed 's/netbook/handset/' -i handset.repo
    $ zypper refresh # at this point you will probably have a security alert, ignore it
    $ zypper install meegotouch-inputmethodbridges meegotouch-inputmethodkeyboard meegotouch-theme meegotouch-theme-meego libmeegotouch-qtstyle meegotouch-systemui

2\. To avoid a weird parsing bug, comment out line 715 in /usr/share/themes/base/meegotouch/libmeegotouchcore/style/commonlayouts.css Do that by (also in the terminal), doing:

    vim /usr/share/themes/base/meegotouch/libmeegotouchcore/style/commonlayouts.css

and then typing :715 and then using insert mode (press 'i') so you can type text. Add a /\* and \*/ before and after the line. When done, press ESC key a few times and then :x to exit and save.

3\. Then you're doing to change how the meego UI/desktop thing loads.

    vim /etc/xdg/autostart/meego-im-uiserver.desktop 

Then change the Exec=\*blah blah\* line to say:

    Exec=/usr/bin/meego-im-uiserver -target slate -bypass-wm-hint

Then change the OnlyShowIn line to have X-MEEGO-NB at the end after the X-MEEGO-HS seperating them by a ; (colon). When done, press ESC key a few times and then :x to exit and save.

OK, now if you restart you would have a keyboard.. But let's make one more mod so it's even better...

4\. Let's make the keyboard transparent so you don't lose have your screen.. Go back to the terminal and run:

    vim /usr/share/themes/base/meegotouch/svg/meegotouch-keyboard.svg

Somewhere in the first few lines you'll see something similar to:

    <svg version="1.1"
      id="meegotouch-keyboard-layer"
      viewBox="0 0 500 480"
      style="enable-background:new 0 0 500 480; opacity:0.4"
      xml:space="preserve">

Except your version don't have "opacity:0.4" ..which is the part you'll add. Just throw it at the end of the line using the same commands as before. I recommend "opacity:0.2" instead of the meego recommended 0.4

5\. Now restart. Type "reboot" at the command line
