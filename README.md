# conj
[![PyPI version](https://badge.fury.io/py/conj.svg)](https://badge.fury.io/py/conj)
[![Build Status](https://travis-ci.org/halilkaya/conj.svg?branch=master)](https://travis-ci.org/halilkaya/conj)
[![Coverage Status](https://coveralls.io/repos/github/halilkaya/conj/badge.svg?branch=master)](https://coveralls.io/github/halilkaya/conj?branch=master)
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
conj(word, properName=False, conjType='dative')
```

 - **word** *(String)*: Word you want to conjugate.
 - **properName** *(Boolean)*: Determining if the word is a proper name to put apostrophe.
 - **conjType** *(String)*: Conjugation type:
   - dative
   - accusative
   - adessive
   - ablative
   - derivative
   - abesive
   - genitive
   - plural

## Conjugation Types
| conjType       | shortcut   | desc                       | example         |
| -------------- | ---------- | -------------------------- | --------------- |
| dative         | e          | -e hâli (yönelme hâli)     | İstanbul'a      |
| accusative     | i          | -i hâli (belirtme hâli)    | İstanbul'u      |
| adessive       | de         | -de hâli (bulunma hâli)    | İstanbul'da     |
| ablative       | den        | -den hâli (ayrılma hâli)   | İstanbul'dan    |
| derivative     | li         | -li hâli (köken)           | İstanbullu      |
| abesive        | siz        | -siz hâli (gıyapta)        | İstanbul'suz    |
| genitive       | in         | -in hâli (âidiyet, ilişki) | İstanbul'un     |
| plural         | ler        | çoğul hâl                  | İstanbul'lar    |

## Contributors
 - [Halil Kaya](https://github.com/halilkaya)
 - [Fatih Erikli](https://github.com/fatiherikli)

## Contributing
 - You can open an issue or send pull request about my faults.
 - You can add new conjugation types via sending pull request.
 - Python2.7 support

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
