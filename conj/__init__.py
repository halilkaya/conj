#!/usr/bin/env python
#-*- coding: UTF-8 -*-

class Conj(object):

    def __init__(self):
        self.VOWEL_LETTERS = [
            'a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü'
        ]
        self.VOWELS = {}
        self.VOWELS['dative'] = \
        self.VOWELS['adessive'] = \
        self.VOWELS['ablative'] = {
            'a': 'a', 'e': 'e', 'ı': 'a', 'i': 'e',
            'o': 'a', 'ö': 'e', 'u': 'a', 'ü': 'e'
        }
        self.VOWELS['accusative'] = {
            'a': 'ı', 'e': 'i', 'ı': 'ı', 'i': 'i',
            'o': 'u', 'ö': 'ü', 'u': 'u', 'ü': 'ü'
        }
        self.SOFTENINGS = {}
        self.SOFTENINGS['dative'] = \
        self.SOFTENINGS['accusative'] = {
            'k': 'ğ'
        }
        self.SOFTENINGS['adessive'] = \
        self.SOFTENINGS['ablative'] = {
            'k': 'k'
        }
        self.EXCEPTIONS = {}
        self.EXCEPTIONS['dative'] = {
            'ben': 'bana',
            'sen': 'sana',
            'o': 'ona'
        }
        self.EXCEPTIONS['accusative'] = {
            'o': 'onu'
        }
        self.EXCEPTIONS['adessive'] = {
            'o': 'onda'
        }
        self.EXCEPTIONS['ablative'] = {
            'o': 'ondan'
        }
        self.HANDLERS = {
            # 0: infix for words ending with a vowel
            # 1: infix for words ending with not a vowel
            # 2: infix if last letter in SOFTENINGS
            # 3: extra last letter if needed
            'dative':     ['y', '', '', ''],
            'accusative': ['y', '', '', ''],
            'adessive':   ['d', 'd', 't', ''],
            'ablative':   ['d', 'd', 't', 'n']
        }

    def getLastLetter(self, word):
        return word[-1].lower()

    def getLastVowel(self, word):
        for letter in reversed(word.lower()):
            if letter in self.VOWEL_LETTERS:
                return letter

    def getSuffix(self, word, conjType):
        lv = self.getLastVowel(word)
        if lv:
            return self.VOWELS[conjType][lv]

    def conjugate(self, word, properName=False, conjType='dative'):
        if not properName and word in self.EXCEPTIONS[conjType]:
            return self.EXCEPTIONS[conjType][word]
        ll = self.getLastLetter(word)
        suffix = self.getSuffix(word, conjType)
        if suffix:
            if ll in self.VOWEL_LETTERS:
                infix = self.HANDLERS[conjType][0]
            elif ll in self.SOFTENINGS[conjType]:
                infix = self.HANDLERS[conjType][2]
            else:
                infix = self.HANDLERS[conjType][1]
            lastLetter = self.HANDLERS[conjType][3]
            if properName:
                return '%s\'%s%s%s' % (word, infix, suffix, lastLetter)
            else:
                if ll in self.SOFTENINGS[conjType]:
                    word = '%s%s' % (word[:-1], self.SOFTENINGS[conjType][ll])
                return '%s%s%s%s' % (word, infix, suffix, lastLetter)
        return word
