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

#numbers

NUMBERS = {'0': 'sıfır',
    '1': 'bir',
    '2': 'iki',
    '3': 'üç',
    '4':'dört',
    '5': 'beş',
    '6': 'altı',
    '7': 'yedi',
    '8': 'sekiz',
    '9': 'dokuz',
    '10': 'on',
    '20': 'yirmi',
    '30': 'otuz',
    '40': 'kırk',
    '50': 'elli',
    '60': 'altmış',
    '70': 'yetmiş',
    '80': 'seksen',
    '90': 'doksan',
    '00': 'bin',
    '000': 'bin',
    '0000': 'bin',
    '00000': 'bin',
    '000000': 'milyon',
    '0000000': 'milyon',
    '00000000': 'milyon',
    '000000000': 'milyar',
    '0000000000': 'milyar',
    '00000000000': 'milyar'}

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

    def conjNumber(self, word):
        properName = True
        word = str(word)[::-1]
        if word[0] in NUMBERS:
            if word[0] != '0':
                word = NUMBERS.get(str(word[0]))
                return word
            else:
                if word[0] == '0' and word[1] != '0':
                    word = NUMBERS.get(str((word[:2])[::-1]))
                    return word
                elif word[0] == '0' and word[1] == '0':
                    zero_count = 0
                    for digit in word:
                        if digit == '0':
                            zero_count += 1
                        else:
                            break
                    word = NUMBERS['0' * zero_count]
                    return word

    def conjugate(self, word, properName=False, conjType='e'):
        word_as_number = None
        if isinstance(word,int):
            word_as_number = str(word)
            word = self.conjNumber(word)

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

                if word_as_number:
                    word = word_as_number

                return ''.join([word, apostrophe, infix, suffix, lastLetter])
            else:
                if conjType in SOFTENINGS and ll in SOFTENINGS[conjType]:
                    word = ''.join([word[:-1], SOFTENINGS[conjType][ll]])

                return ''.join([word, infix, suffix, lastLetter])

        return word

    __call__ = conjugate

conj = Conj()
