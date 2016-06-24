#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals


VOWEL_LETTERS = [
    'a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü', 'û', 'â'
]


# Vowels

VOWELS = {}

VOWELS['e'] = \
VOWELS['de'] = \
VOWELS['den'] = \
VOWELS['ler'] = \
VOWELS['mek'] = {
    'a': 'a', 'e': 'e', 'ı': 'a', 'i': 'e',
    'o': 'a', 'ö': 'e', 'u': 'a', 'ü': 'e'
}

VOWELS['i'] = \
VOWELS['li'] = \
VOWELS['siz'] = \
VOWELS['in'] = {
    'a': 'ı', 'e': 'i', 'ı': 'ı', 'i': 'i',
    'o': 'u', 'ö': 'ü', 'u': 'u', 'ü': 'ü'
}


# Softenings

SOFTENINGS = {}

SOFTENINGS['e'] = \
SOFTENINGS['i'] = \
SOFTENINGS['in'] = {
    'k': 'ğ'
}

SOFTENINGS['de'] = \
SOFTENINGS['den'] = {
    'f': 'f',
    's': 's',
    't': 't',
    'k': 'k',
    'ç': 'ç',
    'ş': 'ş',
    'h': 'h',
    'p': 'p'
}


# Exceptions

EXCEPTIONS = {}

EXCEPTIONS['e'] = {
    'ben': 'bana',
    'sen': 'sana',
    'o': 'ona'
}

EXCEPTIONS['i'] = {
    'o': 'onu'
}

EXCEPTIONS['de'] = {
    'o': 'onda'
}

EXCEPTIONS['den'] = {
    'o': 'ondan'
}

EXCEPTIONS['in'] = {
    'ben': 'benim',
    'biz': 'bizim'
}

EXCEPTIONS['ler'] = {
    'o': 'onlar'
}


# Handlers

UPPER_MAP = {
    ord('i'): 'İ'
}

HANDLERS = {
    # 0: infix for words ending with a vowel
    # 1: infix for words ending with not a vowel
    # 2: infix if last letter in SOFTENINGS
    # 3: extra last letter if needed
    'e':    ['y', '', '', ''],
    'i':    ['y', '', '', ''],
    'de':   ['d', 'd', 't', ''],
    'den':  ['d', 'd', 't', 'n'],
    'li':   ['l', 'l', 'l', ''],
    'siz':  ['s', 's', 's', 'z'],
    'in':   ['n', '', '', 'n'],
    'ler':  ['l', 'l', '', 'r'],
    'mek':  ['m', 'm', '', 'k']
}


class Conj(object):

    def getLastLetter(self, word):
        return word[-1].lower()

    def getLastVowel(self, word):
        for letter in reversed(word.lower()):
            if letter in VOWEL_LETTERS:
                return letter

    def getSuffix(self, word, conjType):
        lv = self.getLastVowel(word)

        if lv:
            ll = self.getLastLetter(word)

            if ll == 'l' and lv == 'â':
                lv = 'e'
            elif ll == 'l' and lv == 'û':
                lv = 'ü'
            elif lv == 'â':
                lv = 'a'
            elif lv == 'û':
                lv = 'u'

            return VOWELS[conjType][lv]

    def makeProperName(self, word):
        if len(word) > 0:
            return ''.join([word[0].translate(UPPER_MAP).upper(), word[1:]])

    def conjugate(self, word, properName=False, conjType='e'):
        if not properName and \
           conjType in EXCEPTIONS and \
           word in EXCEPTIONS[conjType]:
            return EXCEPTIONS[conjType][word]

        ll = self.getLastLetter(word)
        suffix = self.getSuffix(word, conjType)

        if suffix:
            if ll in VOWEL_LETTERS:
                infix = HANDLERS[conjType][0]
            elif conjType in SOFTENINGS and ll in SOFTENINGS[conjType]:
                infix = HANDLERS[conjType][2]
            else:
                infix = HANDLERS[conjType][1]

            lastLetter = HANDLERS[conjType][3]

            if properName:
                word = self.makeProperName(word)

                apostrophe = ''
                if conjType != 'li':
                    apostrophe = '\''

                return ''.join([word, apostrophe, infix, suffix, lastLetter])
            else:
                if conjType in SOFTENINGS and ll in SOFTENINGS[conjType]:
                    word = ''.join([word[:-1], SOFTENINGS[conjType][ll]])

                return ''.join([word, infix, suffix, lastLetter])

        return word

    __call__ = conjugate

conj = Conj()
