Locally-hosted website for access control, webcams, toolshare, and other resources.

Accessible at <http://172.22.110.15>

Future:

- Media player
- Lab wishlist
- Clock with "last call for food," "open/close" and "midnight" bells
- Who's working on what (like a public todo list to help focus and direct)

## Intranet access

To add someone to the users database:

- Run /home/access/ruby sha.rb "USERPASSWORD"
  - Replace USERPASSWORD with the user's desired password.
  - Copy the output
- vim /home/access/users.json
  - Highlight the first user's line and type yyp to duplicate.
  - Change the username and password hash to match the desired username and the hash you copied earlier. (Press i to enter edit mode, esc to exit.)
  - Save and Exit vim by pressing esc :x (or :q! to quit without saving.)
