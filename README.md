# rd_api_py

Python library for Real Debrid API

## Usage

Set `RD_APITOKEN` in `.env`

All operations are supported - see examples directory

```
#!/usr/bin/env python3

from rd_api_py.rdapi import *


print(RD().system.time().content)

print(RD().user.get().json())

print(RD().torrents.get(limit=10, page=1).json())

import os
filepath = os.getcwd() + '/examples/bbb.torrent'
print(RD().torrents.add_file(filepath=filepath).json())

...

```