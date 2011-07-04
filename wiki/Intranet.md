Locally-hosted website for access control, webcams, toolshare, and other resources.

Accessible at <http://172.22.110.15>

Future:

- Media player
- Lab wishlist
- Clock with "last call for food," "open/close" and "midnight" bells
- Who's working on what (like a public todo list to help focus and direct)

## Intranet access

To add someone to the users database:

- Run ruby /home/access/sha.rb "USERPASSWORD" \>\> hash.txt && clear
  - Have the user replace USERPASSWORD with the user's desired password and press enter.
  - Copy the output from hash.txt
- vim /home/access/users.json
  - Highlight the first user's line and type yyp to duplicate.
  - Change the username and password hash to match the desired username and the hash you copied earlier. (Press i to enter edit mode, esc to exit.)
  - Save and Exit vim by pressing esc :x (or :q! to quit without saving.)

Send them these instructions:

You've been added to the intranet system!

Just connect to the wifi: HeatSync Labs, password hacktheplanet .

Point a web browser to <http://172.22.110.15> .

Click on Access Control.

Username is USER password is whatever you typed.

You have access to open the front and back door, as well as lock and unlock all doors.

If they are an admin, modify the last line to read:

You have full access to open, lock, and unlock all doors as well as arm and disarm the alarm.
