# conj
[![PyPI version](https://badge.fury.io/py/conj.svg)](https://badge.fury.io/py/conj)
[![Build Status](https://travis-ci.org/halilkaya/conj.svg?branch=master)](https://travis-ci.org/halilkaya/conj)
[![Coverage Status](https://coveralls.io/repos/github/halilkaya/conj/badge.svg?branch=master)](https://coveralls.io/github/halilkaya/conj?branch=master)
[![Code Health](https://landscape.io/github/halilkaya/conj/master/landscape.svg?style=flat)](https://landscape.io/github/halilkaya/conj/master)
[![GPL Licence][licence-badge]](LICENSE)

Python conjugation module for Turkish.

## Installation
```sh
$ pip install conj
```

## Usage Example
```python
from conj import conj

print(conj('İstanbul', True, 'den'))  # output: İstanbul'dan
print(conj('Muş', True, 'de'))  # output: Muş'ta

# -----------------------------------------------------------

import random
title = "%(name)s %(punishment)s şoku"
names = ['Guido', 'Merkel', 'Voyvoda']
punishments = ['Hapis', 'Kazık']

print title % {
  "name": conj(random.choice(names), True, 'e'),
  "punishment": random.choice(punishments)
}

# output: Guido'ya hapis şoku
# output: Merkel'e hapis şoku
# output: Voyvodo'ya kazık şoku

```

## Supported Python Versions
 - python 3
 - python 2
 - pypy3
 - pypy

## Running Tests
To run tests, you have to install **unittest** first:
```sh
$ pip install unittest
```
Then, just run **tests.py**:
```sh
$ python tests.py
```

## API Reference

### `conj`
```python
conj(word, properName=False, conjType='e')
```

 - **word** *(String)*: Word you want to conjugate.
 - **properName** *(Boolean)*: Determining if the word is a proper name to put apostrophe.
 - **conjType** *(String)*: See the conjugation types table below.

## Conjugation Types
| conjType   | desc                             | example         |
| ---------- | -------------------------------- | --------------- |
| e          | -e, -a (yönelme hâli)            | İstanbul'a      |
| i          | -i, -ı, -ü, -u (belirtme hâli)   | İstanbul'u      |
| de         | -de, -da (bulunma hâli)          | İstanbul'da     |
| den        | -den, -dan (ayrılma hâli)        | İstanbul'dan    |
| li         | -li, -lı (köken)                 | İstanbullu      |
| siz        | -siz, -sız (gıyapta)             | İstanbul'suz    |
| in         | -in, -ın (âidiyet, ilişki)       | İstanbul'un     |
| ler        | -ler, -lar (çoğul hâl)           | atlar           |
| mek        | -mek, -mak (mastar)              | gezmek          |

## Contributors
 - [Halil Kaya](https://github.com/halilkaya)
 - [Fatih Erikli](https://github.com/fatiherikli)
 - [Emin Mastizada](https://github.com/mastizada)
 - [Cemal Eker](https://github.com/cemaleker)

## Contributing
 - You can open an issue or send pull request about my faults.
 - You can add new conjugation types via sending pull request.

## License
```
Python conjugation module for Turkish.
Copyright (C) 2016  Halil Kaya

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
[See Full License](https://github.com/halilkaya/conj/blob/master/LICENSE)

[licence-badge]:http://img.shields.io/badge/licence-GPL-brightgreen.svg
