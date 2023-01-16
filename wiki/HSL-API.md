Space to document the functionality of the new HSL API

Features:

## People

- Ability to see a list of Users (people/members)
- Ability to add a new User
- Ability to merge Users
- Ability to edit User
- Ability to view User details (lot of information here)

## Tools & Resources

## Certifications

- List certification classes
- Ability to create a class certification
- Ability to view User certifications
  - Ability to view certifications by class
  - Ability to add a new User certification

## Waivers

- Ability to see who has filled out a waiver
- Ability to see when the waiver was filled out
- Ability to view waiver
- Ability to edit waiver

## Doors

- Access cards
  - New Card
  - Upload all cards
  - List users with card access
  - Ability to disable card
  - Ability to replace card
- Door Logs
- Space API
- Remote Door Access

### Current status of the door sub-project

- **Current setup:** ACCX version 2, which is a door access shield attached to an Arduino Ethernet and customized firmware to take commands over HTTP <https://www.accxproducts.com/content/category/open-source-hardware/page/3> if flashed with a standard firmware, the Arduino would repond to the same serial/usb/gpio commands as ACCX 4. Touching this system may result in messing up door access for HSL members, so should only be done with extreme care and substantial knowledge/communication. The current members.hsl Rails app talks with the Arduino Ethernet over a rudimentary and insecure HTTP protocol.

<!-- -->

- **Proposed setup:** ACCX version 4, which has an onboard Arduino Mega in addition to expanded access control hardware (check the wiki for precise details) <https://www.accxproducts.com/wiki/index.php?title=Open_Access_4.0> it talks with an attached Linux computer (raspi, etc) over either GPIO or USB, but to get internet connectivity or one-click database synchronization it needs an additional component running on said Linux computer to translate the serial to http and back. Duncan has written this portion, and it's technically superior.

## Computers

- List of MAC addresses on the network
- Ability to purge old records

## Payments

- List view of payment
- Ability to view payment details
- Ability to edit payment
- Ability to create a manual payment

Note: This list was copied from the old members site menu. Please expand on each section as needed.
