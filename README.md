# rd_api_py

Real Debrid API Library for Python

## Installation

Install the package.
```bash
python -m pip install rd_api_py
```

Set `RD_APITOKEN` `.env` in `rd_refresh` or your script

## Usage

All operations are supported - see examples directory

```python
from rdapi import RD

RD = RD()

print(RD.system.time().content)
print(RD.user.get().json())
print(RD.torrents.get(limit=10, page=1).json())

import os
filepath = '/path/to/bbb.torrent'
print(RD.torrents.add_file(filepath=filepath).json())

# etc...
```