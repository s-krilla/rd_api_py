# rd_api_py

Real Debrid API Library for Python

## Installation

Install the package

```bash
python -m pip install rd_api_py
```

Set `.env` environment variables in `rd_refresh` or your script

```bash
RD_APITOKEN="your_token_here"

# Optional, defaults recommended
SLEEP=2000 # Delay (ms) between requests 
LONG_SLEEP=30000 # Long delay (ms) every 500 requests
```

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