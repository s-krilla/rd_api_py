# rd_api_py

Python library for Real Debrid API

## Installation

Set `RD_APITOKEN` in `.env`. 

Install the package.
```bash
cd rd_api_py
pip install -e .
```

## Usage

All operations are supported - see examples directory

```python
from rdapi import RD

print(RD().system.time().content)
print(RD().user.get().json())
print(RD().torrents.get(limit=10, page=1).json())

import os
filepath = '/path/to/bbb.torrent'
print(RD().torrents.add_file(filepath=filepath).json())

# etc...
```