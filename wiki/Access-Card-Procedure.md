## Access Cards

### New Member

- Members can receive cards when approved by a majority vote of members at an operations meeting ("Hack your Hackerspace" night.) Ensure their card access proposal is posted publicly via email (subject prefix "Proposal:") at least 1 week prior to the meeting.
  - An [example of a proposal](https://groups.google.com/forum/?fromgroups=#!searchin/heatsynclabs/proposal$20brooks/heatsynclabs/Is9dKu2nL10/bpruN_vqsWUJ) may be found in the archives, but in general should stress how the person fits in the community, what projects they work on, what service they've done, and how they hold our values.
- Login to [hsl-access](Hsl-access) via SSH
- Run minicom
  - If you haven't set your settings yet, it must be /dev/ttyUSB0 57600 8N1.
- Type e \#### where \# is the enable password.
- Type a for a list of all users.
- Find the first entry with a usermask of 255 after user \#10 (users 0-9 are for testing.)
- Check the Access Control System Card Database.txt file in Dropbox.
  - Log which user# you're going to use, in this format:
    - UserNumber UserMask TagNumber FirstName LastName
    - I.e.: 9 1 a1b2c3d4 John Smith
    - Usermask 1 is "full access", 255 is "no access."
- Type m followed by the user#, usermask, and tagnumber.
  - Make sure you're not overwriting an existing user# and copy-paste to avoid typos because a typo can easily overwrite an unexpected user#.
  - I.e. m 9 1 a1b2c3d4
- Exit minicom by typing ctrl+a,x and double-check the status of the doors as they may have re-locked themselves.

### Member Nonpayment/Cancellation

- It's a good idea for the member to have a Basic (\$50/mo) membership.
- Members cards are deactivated / reactivated upon notice of nonpayment or other issues from the Treasurer.
- Check the Access Control System Card Database.txt file in Dropbox.
  - Find the user's entry in the list, and update their UserMask to be 255 ("no access") instead of 1 ("full access") or vice versa.
    - I.e.: 9 255 a1b2c3d4 John Smith
- Login to [hsl-access](Hsl-access) via SSH
- Run minicom
  - If you haven't set your settings yet, it must be /dev/ttyUSB0 57600 8N1.
- Type e \#### where \# is the enable password.
- Type m followed by the user#, usermask, and tagnumber.
  - Copy-paste to avoid typos because a typo can easily overwrite an unexpected user#.
  - I.e. m 9 255 a1b2c3d4
- Exit minicom by typing ctrl+a,x and double-check the status of the doors as they may have re-locked themselves.
