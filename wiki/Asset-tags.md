## Overview

*Note: Approved by vote at the 2021-08-26 Hack Your Hackerspace*

There needs to be a way to track HSL assets. This is helpful for a number of reasons:

- Helps with managing [Inventory](Inventory)
- Allows us to document donations and any restrictions on usage/disposal
- Potentially document the life-cycle of items

The tag design requirements are:

- Reasonable size
  - Small enough to fit on most equipment
  - Large enough to be readable/findable
- Serialized (i.e. unique numbers)
- Ability to store data about the asset
- Durable

## What Gets an Asset Tag

Things that need them. Seriously, let's try to be reasonable. Here are some guidelines:

- Significant equipment
- Physically large donations
- Equipment on long-term loan to HSL

## What Wouldn't Get a Tag

- Consumables
- Hand tools
- Members

## Proposed Tag

![](files/Asset-tag-prototype.png)

*asset-tag-prototype.png*

QR code and link point to a page for details.

This tag would be printed out on a durable material and then put on the asset.

### Location

The tag should be placed as close to the serial number as is reasonable.

### Additional Thoughts

Although we briefly considered doing RFID tags or something similar, for the purposes of what we're trying to do, KISS is probably a better place to start.

## Data storage

Each of the assets will be stored in a spreadsheet (Google sheet) to allow for tracking and management.

### Proposed Data Fields

- Asset tag number
- Description
- Date acquired
- Station it belongs to
- Owner (HSL or other)
- Is it a long term loan?
- Disposal requirements (e.g. for donated items)
- Requires training
- Whatever else

### Example

- [Google sheet](https://docs.google.com/spreadsheets/d/1gctZysF9LWCdm0eKXy08uFr6eEs-peLb-nx2_6lBaAA/edit?usp=sharing)
