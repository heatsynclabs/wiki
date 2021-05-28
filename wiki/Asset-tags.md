## Overview

There needs to be a way to track HSL assets. The design requirements are:

- Reasonable size
  - Small enough to fit on most equipment
  - Large enough to be readable/findable
- Serialized (i.e. unique numbers)
- Ability to store data about the asset
- Durable

## Proposed Tag

![](files/Asset-tag-prototype.png)

*asset-tag-prototype.png*

QR code and link point to a page for details.

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
